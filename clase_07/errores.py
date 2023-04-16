# print(10/0)
# # ZeroDivisionError: division by zero

# 2 * x - 2
# # NameError: name 'x' is not defined

# print('2'+5)
# # TypeError: can only concatenate str (not "int") to str

# try:
#     x = int(input("Ingrese un dividendo entero: "))
#     y = int(input("Ingrese un divisor entero: "))
#     print(x/y)
# except (ValueError, ZeroDivisionError):
#     print("No ingresó un número entero válido o está intentando dividir por CERO")
# finally:
#     print("Fin del programa")


# Ingrese un dividendo entero: 2
# Ingrese un divisor entero: 3
# 0.6666666666666666
# Fin del programa

# file = open('archivo.txt', 'x')
# for linea in file:
#     if 'linea' in linea:
#         print(linea)

# file = open('archivo_2.txt', 'w')
# file.write("Vamos a agregar una linea a nuestro archivo txt")
# print(file._checkClosed('archivo_2.txt'))

import os

os.remove('archivo_2.txt')

import os

if os.path.exists("archivo_2.txt"):
  os.remove("archivo_2.txt")


""" EJERCICIOS """
# Hacer que la ticketera cree un ticket nuevo al finalizar cada compra
# Poder eliminar un ticket cualquiera
# Ver todos los tickets