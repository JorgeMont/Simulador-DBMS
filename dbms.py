#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Monterrosas Ramírez Jorge
#Delgadillo Cortez Hugo

#METER EN FUNCIONES :P
#----------------------------------------------------INSERT----------------------------------------
#def update(posicion,tupla):

comando = input()
#Espera una entrada de teclado que guarda como variable para los comandos

comando = comando.lower()
#transforma a minuscula

comando = comando.split(' ')
#separa los elementos del comando por espacios
#----------------------------------------------------SELECT----------------------------------------
file = open('bd_empleados.txt','r')
if comando[0] == 'select':
    #Si el primer elemento del comando es un select entonces...
    if comando[1] == '*' :
        #cuando el segundo elemento del comando es *
        if comando[2] == 'from' and comando[3] == 'empleados':
            for line in file:
                print(line)
        elif comando[2] == 'from' and comando[3] != 'empleados':
            print('Tabla no encontrada...')
        else: 
            print('comando erroneo...')

    elif comando[1] == 'id':
         #cuando el segundo elemento del comando es id
        if comando[2] == 'from' and comando[3] == 'empleados':
            for line in file:
                #muestra la consulta
                registro = line.split(',')
                print(registro[0])
        elif comando[2] == 'from' and comando[3] != 'empleados':
            print('Tabla no encontrada...')
        else: 
            print('comando erroneo...')   
        
    elif comando[1] == 'nombre':
        #cuando el segundo elemento del comando es nombre
        if comando[2] == 'from' and comando[3] == 'empleados':
            for line in file:
                #muestra la consulta
                registro = line.split(',');
                print(registro[1])
        elif comando[2] == 'from' and comando[3] != 'empleados':
            print('Tabla no encontrada...')
        else: 
            print('comando erroneo...')
    
    elif comando[1] == 'appat':
        #cuando el segundo elemento del comando es appat
        if comando[2] == 'from' and comando[3] == 'empleados':
            for line in file:
                #muestra la consulta
                registro = line.split(',');
                print(registro[2])
        elif comando[2] == 'from' and comando[3] != 'empleados':
            print('Tabla no encontrada...')
        else: 
            print('comando erroneo...')

    elif comando[1] == 'apmat':
        #cuando el segundo elemento del comando es apmat
        if comando[2] == 'from' and comando[3] == 'empleados':
            for line in file:
                #muestra la consulta
                registro = line.split(',');
                print(registro[3])
        elif comando[2] == 'from' and comando[3] != 'empleados':
            print('Tabla no encontrada...')
        else: 
            print('comando erroneo...')
        
    elif comando[1] == 'dept_id':
       #cuando el segundo elemento del comando es dept_id
        if comando[2] == 'from' and comando[3] == 'empleados':
                for line in file:
                    #muestra la consulta
                    registro = line.split(',');
                    print(registro[4])
        elif comando[2] == 'from' and comando[3] != 'empleados':
            print('Tabla no encontrada...')
        else: 
            print('comando erroneo...')

    elif comando[1] == 'salario':
        #cuando el segundo elemento del comando es salario
        if comando[2] == 'from' and comando[3] == 'empleados':
                for line in file:
                    #muestra la consulta
                    registro = line.split(',');
                    print(registro[5])
        elif comando[2] == 'from' and comando[3] != 'empleados':
            print('Tabla no encontrada...')
        else: 
            print('comando erroneo...')
    file.close()
#----------------------------------------------------INSERT----------------------------------------
elif comando[0] == 'insert' and comando[1] == 'into': # si el promer comando es insert y el segundo es un into se reconoce la orden
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
        file.write(str(v_id) + ',' + v_nom + v_appat + v_apmat + v_deptid + v_sal + '\n')
        file.close()
    else:
        print('Tabla no encontrada...')    
#---------------------------------------------------UPDATE---------------------------------------------------------
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
            #contenido = contenido + 'el cincooo ajajajjaa \n'
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

#-------------------------------DELETE----------------------------------------------   
elif comando[0] == 'delete' and comando[1] == 'from':
    #Si el primer elemento del comando es un insert entonces...
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


else:
    #Muestra error cuando no se insertan comandos validos
    print('Error, comando no valido...')
file.close()