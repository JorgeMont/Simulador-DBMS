# archivo = open("bd_empleados.txt", "r+")
# indice = 0
# contenido = ''
# for line in archivo:
#     tupla = line
#     if indice == 5:
#         contenido = contenido + 'el cincooo ajajajjaa \n'
#         #print(len(tupla))
#     else:
#         contenido = contenido + tupla
#         #print(len(tupla))
#     indice += 1
# print(contenido)        
# archivo.close()



# #------------------------
# elif comando[0] == 'delete' and comando[1] == 'from':
#     #Si el primer elemento del comando es un insert entonces...
#     archivo = open("bd_empleados.txt", "r+")
#     indice = 0
#     pk_delete = int(comando[6])
#     contenido = ''
#     for line in archivo:
#         tupla = line
#         if indice == pk_delete:
#             #aqui va lo de eliminar la fila
#             #meter un pass y ver como seguir con los indices
#             pass
             
#         else:
#             contenido = contenido + tupla
#             #print(len(tupla))
#         indice += 1
#     #print(contenido)        
#     archivo.close()
#     archivo = open('bd_empleados.txt', 'w')
#     archivo.write(contenido)
#     archivo.close()
#------------------------------------------------
#recibimos la ip y el puerto
# parametros = str(input("Indique IP y puerto: ")).split(" ")
# #Lo convertimos en cadena, lo separamos como lista para tener dos elementos, la ip y el puerto
# print(parametros[0]) #la ip
# print(parametros[1]) #el puerto
archivo = open("bd_empleados.txt", "r+")
contenido = archivo.readlines()
print(contenido)

archivo.close()