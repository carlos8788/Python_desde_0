""" CONSIDERAR USAR LO QUE VIMOS EN LA CLASE 3"""

# Ingresar desde la consola 3 números y devolver por consola esa lista ordenada de mayor a menor y de menor a mayor

# Crear una función que sume los números ingresados en la lista anterior.

# Crear una función que dado 2 números cualquiera devuelva todos los números comprendidos entre si (solamente los enteros)

# def rango(a, b):
#     if a > b:
#         while b < a:
#             b +=1
#             print(b)
            
#     else:
#         while a < b:
#             print(a)
#             a +=1

# rango(1, 5)
# print("***"*9)
# rango(9, 2)

# lista = ['a', 'b', 'c', 'd', 3]
# print(len(lista)) # 5

# diccionario = {1: "Lengua", 2:"Matemáticas", 3:"Historia", 4:"Informática"}
# print(len(diccionario)) # 4

# for i in range(2, 10, 2):
#     print(i)
#2
#4
#6
#8

# palabra = "Hola"

# print("a" in palabra) # True
# print("c" in palabra) # False
# print("a" not in palabra) # False

# diccionario = {1: "Lengua", 2:"Matemáticas", 3:"Historia", 4:"Informática"}
# if 4 in diccionario.keys():
#     print("Si está") # Si está
# else:
#     print("No está")

# diccionario = {1: "Lengua", 2:"Matemáticas", 3:"Historia", 4:"Informática"}
# if "Lengua" in diccionario.values():
#     print("Si está") # Si está
# else:
#     print("No está")

import modulo_arit as m_ar

print(m_ar.sumar(2, 5))