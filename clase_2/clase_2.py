""" LISTAS """
# lista.pop(2)
# print(lista) # [1, 2, 4]

lista = ['a', 'z', 'c', 'b']
lista.sort()
# print(lista)
lista.reverse()
# print(lista, "método reverse")

lista_2 = [10, 20, 123, 5, 2, 4]

# lista_2.remove(5)
lista_2.pop(5)
# print(lista_2)

lista_0 = [1, 2, 3, 4]
lista_0.append(5)
lista_0.count(1)
# print(lista_0, "lista")

""" TUPLAS """
tupla_0 = (1, 2, 3, 4)
# print(tupla_0.index(4))
# print(tupla_0, 'tupla')

""" DICCIONARIOS """
diccionario = {
    "Nombre": "Francisco",
    "Edad": 27,
    "Documento": 123456,
    "Celular": 123456
}

print(id(diccionario)) # {'Nombre': 'Francisco', 'Edad': 27, 'Documento': 123456, 'Celular': 123456}

diccionario.update({'Dirección': 'Av. Siempre Viva 123'})
print(diccionario)


