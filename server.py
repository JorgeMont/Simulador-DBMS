import socket
import sys
#importamos lo necesario para trabajar con sockets
def cadenita(cliente):
        #funcion de prueba
        #nuestra_respuesta = str(input(">>"))
        nuestra_respuesta = 'id,nombre,appat,apmat,dept_id,salario \n 1,jorge,monterrosas,ramirez,1,20000'
        cliente.send(nuestra_respuesta.encode('utf-8'))

        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Creamos un objeto tipo socket
s.bind(("", 8080 ))
#Lo enlazamos a la ip que queda vacia para recibir clientes externos al localhost, y al puerto
s.listen(5)
#Maximo de peticiones encoladas
 
print ("Servidor de Chat\n")
while True: 
        #Siempre esperando una conexion
        print ("Esperando conexión...")
        #con accept() aceptamos las peticiones
        #El primer valor que devuelve es la conexion y el segundo la direccion
        sc, addr = s.accept()
        print ("Cliente conectado desde: ", addr)
 
        while True:
                recibido = sc.recv(1024)
                recibido = recibido.decode('utf-8')
                if recibido == 'quit': #orden para salir
                        print ("Adios")
                        sc.send('quit client'.encode('utf-8'))
                        sc.close()
                        s.close()
                        sys.exit()
                else:
                #        print ("Recibido: ", recibido) #imprime mensaje leido 
                #        nuestra_respuesta = str(input(">>"))
                #        #nuestra_respuesta = "Hola cliente" #manda esta respuesta al cliente
                #        sc.send(nuestra_respuesta.encode('utf-8'))
                        cadenita(sc)

 

 