import socket
import sys
#importamos lo necesario para trabajar con sockets

#DEFINICION DE FUNCION ORACLE
def cadenita(cliente):
        #funcion de prueba
        #nuestra_respuesta = str(input(">>"))
        nuestra_respuesta = 'id,nombre,appat,apmat,dept_id,salario \n 1,jorge,monterrosas,ramirez,1,20000'
        cliente.send(nuestra_respuesta.encode('utf-8'))

def oracle(cliente, comando):
        comando = comando.lower()
        #transforma a minuscula el comando recibido del cliente
        comando = comando.split(' ')
        #separa los elementos del comando por espacios
        #----------------------------------------------------SELECT----------------------------------------
        file = open('bd_empleados.txt','r')
        if comando[0] == 'select':
                #Si el primer elemento del comando es un select entonces...
                if comando[1] == '*' :
                #cuando el segundo elemento del comando es *
                        if comando[2] == 'from' and comando[3] == 'empleados':
                                #for line in file:
                                #MODIFICAR, SOLO SE MANDA UNA LINEA POR SOLICITUD
                                #cliente.send(line.encode('utf-8'))
                                #print(line)
                                contenido = ''
                                for line in file:
                                        contenido = contenido + line
                                cliente.send(contenido.encode('utf-8'))
                        elif comando[2] == 'from' and comando[3] != 'empleados':
                                #print('Tabla no encontrada...')
                                cliente.send('Tabla no encontrada ...'.encode('utf-8'))
                        else: 
                                #print('comando erroneo...')
                                cliente.send('Comando erroneo ...'.encode('utf-8'))
                #cuando el segundo elemento del comando es id
                elif comando[1] == 'id':
                        if comando[2] == 'from' and comando[3] == 'empleados':
                                contenido = ''
                                for line in file:
                                        #muestra la consulta
                                        registro = line.split(',')
                                        #print(registro[0])
                                        contenido = contenido + registro[0] + '\n'
                                cliente.send(contenido.encode('utf-8'))

                        elif comando[2] == 'from' and comando[3] != 'empleados':
                            print('Tabla no encontrada...')
                        else: 
                            print('comando erroneo...')
                #cuando el segundo elemento del comando es el nombre
                elif comando[1] == 'nombre':
                        #cuando el segundo elemento del comando es nombre
                        if comando[2] == 'from' and comando[3] == 'empleados':
                                contenido = ''
                                for line in file:
                                        #muestra la consulta
                                        registro = line.split(',');
                                        #print(registro[1])
                                        contenido = contenido + registro[1] + '\n'
                                cliente.send(contenido.encode('utf-8'))
                        elif comando[2] == 'from' and comando[3] != 'empleados':
                            print('Tabla no encontrada...')
                        else: 
                            print('comando erroneo...')
                #CUANDO EL SEGUNDO ELEMENTO ES EL APELLIDO PATERNO
                elif comando[1] == 'appat':
                        if comando[2] == 'from' and comando[3] == 'empleados':
                                contenido = ''
                                for line in file:
                                        #muestra la consulta
                                        registro = line.split(',');
                                        #print(registro[2])
                                        contenido = contenido + registro[2] + '\n'
                                cliente.send(contenido.encode('utf-8'))
                        elif comando[2] == 'from' and comando[3] != 'empleados':
                                print('Tabla no encontrada...')
                        else: 
                                print('comando erroneo...')
                #CUANDO EL SEGUNDO ELEMENTO ES EL APELLIDO MATERNO
                elif comando[1] == 'apmat':
                        if comando[2] == 'from' and comando[3] == 'empleados':
                                contenido = ''
                                for line in file:
                                        #muestra la consulta
                                        registro = line.split(',');
                                        #print(registro[2])
                                        contenido = contenido + registro[3] + '\n'
                                cliente.send(contenido.encode('utf-8'))
                        elif comando[2] == 'from' and comando[3] != 'empleados':
                                print('Tabla no encontrada...')
                        else: 
                                print('comando erroneo...')
                #CUANDO EL SEGUNDO ELEMENTO ES EL ID DEL DEPARTAMENTO
                elif comando[1] == 'dept_id':
                        if comando[2] == 'from' and comando[3] == 'empleados':
                                contenido = ''
                                for line in file:
                                        #muestra la consulta
                                        registro = line.split(',');
                                        #print(registro[2])
                                        contenido = contenido + registro[4] + '\n'
                                cliente.send(contenido.encode('utf-8'))
                        elif comando[2] == 'from' and comando[4] != 'empleados':
                                print('Tabla no encontrada...')
                        else: 
                                print('comando erroneo...')
                #CUANDO EL SEGUNDO ELEMENTO ES EL APELLIDO SALARIO
                elif comando[1] == 'salario':
                        if comando[2] == 'from' and comando[3] == 'empleados':
                                contenido = ''
                                for line in file:
                                        #muestra la consulta
                                        registro = line.split(',');
                                        #print(registro[2])
                                        contenido = contenido + registro[5] + '\n'
                                cliente.send(contenido.encode('utf-8'))
                        elif comando[2] == 'from' and comando[3] != 'empleados':
                                print('Tabla no encontrada...')
                        else: 
                                print('comando erroneo...')
                
                file.close()


#FIN DE DEFINICION DE FUNCION ORACLE
#---------------------------------------------------
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
                        #cadenita(sc)
                        oracle(sc, recibido)
                        #funcion oracle, recibe el socket del cliente y la cadena que recibe el server

 

 