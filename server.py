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
                            cliente.send('Tabla no encontrada ...'.encode('utf-8'))
                        else: 
                            cliente.send('Comando erroneo ...'.encode('utf-8'))
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
                            cliente.send('Tabla no encontrada ...'.encode('utf-8'))
                        else: 
                            cliente.send('Comando erroneo ...'.encode('utf-8'))
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
                                cliente.send('Tabla no encontrada ...'.encode('utf-8'))
                        else: 
                                cliente.send('Comando erroneo ...'.encode('utf-8'))
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
                                cliente.send('Tabla no encontrada ...'.encode('utf-8'))
                        else: 
                                cliente.send('Comando erroneo ...'.encode('utf-8'))
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
                                cliente.send('Tabla no encontrada ...'.encode('utf-8'))
                        else: 
                                cliente.send('Comando erroneo ...'.encode('utf-8'))
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
                                cliente.send('Tabla no encontrada ...'.encode('utf-8'))
                        else: 
                                cliente.send('Comando erroneo ...'.encode('utf-8'))
                file.close()
        #INSERT---------------------------------------
        elif comando[0] == 'insert' and comando[1] == 'into': 
                # si el primer comando es insert y el segundo es un into se reconoce la orden
                if comando[2] == 'empleados': # verificamos que la tabla sea la unica existente que en este caso es empleados
                        #Leer y validar el VALUES
                        #LOS VALORES A INSERTAR SE GUARDAN EN VARIABLES
                        #calcular el id
                        file = open('bd_empleados.txt','r')
                        v_id = len(file.readlines())
                        file.close()
                        #removemos los primeros caracteres que son el 'values('
                        valores = comando[3]
                        valores = valores[7:]
                        valores = valores.split(",")
                        print(valores)
                        v_nom = valores[0]
                        v_appat = valores[1]
                        v_apmat = valores[2]
                        v_deptid = valores[3]
                        v_sal = valores[4]
                        v_sal = v_sal.replace(")", "")
                        # valores.replace(" ", "")
                        # #la cadena queda unicamente con los valores definitivos a insertar en la BD
                        #print(v_id, v_nom, v_appat, v_apmat, v_deptid, v_sal)
                        file = open('bd_empleados.txt','a')
                        file.write(str(v_id) + ',' + v_nom + ',' + v_appat + ',' + v_apmat + ',' + v_deptid + ',' + v_sal)
                        file.close()
                        cliente.send('Fila agregada'.encode('utf-8'))
                else:
                        cliente.send('Tabla no encontrada...'.encode('utf-8'))   
        #UPDATE----------------------------- 
        elif comando[0] == 'update' and comando[1] == 'empleados' and comando[2] == 'set':
                #Si el primer elemento del comando es un update entonces...
                archivo = open("bd_empleados.txt", "r+")
                indice = 0
                pk_update = int(comando[9])
                contenido = ''
                for line in archivo:
                        tupla = line
                        if indice == pk_update:
                                #aqui va lo de sustituir
                                tupla = tupla.split(',')
                                if comando[3] == 'nombre': #esto para cada campo
                                        tupla[1] = comando[5]
                                        # tupla = str(tupla)
                                        #tupla = str(tupla).translate({ord(i): None for i in '[]"'})
                                        #tupla = str(tupla)
                                        nueva_tupla = ','.join(tupla)
                                        contenido = contenido + nueva_tupla
                                elif comando[3] == 'appat':
                                        tupla[2] = comando[5]
                                        nueva_tupla = ','.join(tupla)
                                        contenido = contenido + nueva_tupla
                                elif comando[3] == 'apmat':
                                        tupla[3] = comando[5]
                                        nueva_tupla = ','.join(tupla)
                                        contenido = contenido + nueva_tupla
                                elif comando[3] == 'dept_id':
                                        tupla[4] = comando[5]
                                        nueva_tupla = ','.join(tupla)
                                        contenido = contenido + nueva_tupla
                                elif comando[3] == 'salario':
                                        tupla[5] = comando[5]
                                        nueva_tupla = ','.join(tupla)
                                        contenido = contenido + nueva_tupla
                        else:
                                contenido = contenido + tupla
                                #print(len(tupla))
                        indice += 1
                #print(contenido)        
                archivo.close()
                archivo = open('bd_empleados.txt', 'w')
                archivo.write(contenido)
                archivo.close()
                cliente.send('Fila actualizada'.encode('utf-8'))
        #DELETE----------------------------- 
        elif comando[0] == 'delete' and comando[1] == 'from':
                archivo = open("bd_empleados.txt", "r+")
                indice = 0
                pk = 0
                pk_delete = int(comando[6])
                contenido = ''
                for line in archivo:
                        #recorre cada linea del archivo para ver cual es el que se debe eliminar
                        if indice == 0:
                                contenido = contenido + line #copia el encabezado
                                indice += 1
                                pk += 1
                        elif indice == pk_delete: ##cuando no es encabezado
                                ##cuando el indice sea la tupla que se quiere borrar
                                indice += 1
                        else:
                                tupla = line.split(',')
                                tupla[0] = str(pk)
                                tupla = ','.join(tupla)
                                contenido = contenido + tupla
                                indice += 1
                                pk += 1
                #print(contenido)        
                archivo.close()
                archivo = open('bd_empleados.txt', 'w')
                archivo.write(contenido)
                archivo.close()
                cliente.send('Fila eliminada'.encode('utf-8'))
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
                if recibido == 'salir': #orden para salir
                        print ("Salio el cliente")
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

 

 