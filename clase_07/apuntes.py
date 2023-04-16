import os
# while True:
#     try:
#         x = int(input("Ingresar un número entero: "))
#         print(f"El número ingresado es: {x}")
#         break
#     except ValueError:
#         print("Error!!!! No ingresó un número entero, intente nuevamente")

# bloc_de_notas = open('archivo.txt', 'r')
# print(bloc_de_notas.readline())
# print(bloc_de_notas.readline())
# bloc_de_notas.close()

# for linea in bloc_de_notas:
#     if 'Segunda' in linea:
#         print(linea)

# Creación de un archivo txt
# try:
#     file = open("archivo_2.txt", "x")
#     file.close()
# except FileExistsError:
#     print("El archivo ya existe")
# finally:
#     print("Finalización de la creacion del txt")

# Escribir texto sobre el archivo
# file = open("archivo_2.txt", "w")
# file.write("Escribiendo desde Python sobre mi txt intento 2")
# file.close()

# Leer un archivo
# try: 
#     file = open("archivo_2.txt", "r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("El archivo no se encontró")
# finally:
#     print("Fin de lectura")

# try: 
#     os.remove('archivo_2.txt')
# except FileNotFoundError as e:
#     # print("Archivo no encontrado", e)
#     print(e)

# print("Continua la ejecución de Python")

file = open('registro.txt', 'r')
lista = []
for i in file:
    lista.append(i)
    
print(lista)