import socket #importamos biblioteca para uso de sockets
import sys #importamos biblioteca para termino de ejecucion de programa

#recibimos la ip y el puerto
parametros = str(input("Indique IP y puerto: ")).split(" ")
#Lo convertimos en cadena, lo separamos como lista para tener dos elementos, la ip y el puerto
#print(parametros[0]) #la ip
#print(parametros[1]) #el puerto

try: #captacion de error de creacion de socket
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as errorsote: #lanzamos error
        print("Fallo la creación del socket con error: %s" %(errorsote))

#modificar para que sea el localhost o alguna ip
try:
        socket_cliente.connect((parametros[0], int(parametros[1]) ))
        #local host es la direccion a la que nos queremos conectar y el puerto
except socket.error as erros_conec:
        print("Error, no se encontro servidor en esa direccion: %s " %(erros_conec))
        sys.exit()
 
while True:
        #Cuando conecta empieza ...
        mensaje = str(input(">> "))
        socket_cliente.send(mensaje.encode('utf-8'))
 
        recibido = socket_cliente.recv(1024)
        #recibe lo que el servidor manda desde su socket
        #el 1024 hace referencia al buffer
        recibido = recibido.decode('utf-8')
        #if recibido == 'gordito':
        #	print('Chiiiii')
        #else:
        print("Recibido: \n", str(recibido))
 
print ("Adios")
socket_cliente.close()
 