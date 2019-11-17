import socket
 
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("localhost", 8080 ))
#local host es la direccion a la que nos queremos conectar y el puerto
 
while True:
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
 