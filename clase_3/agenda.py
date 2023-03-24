# import os
# import time
# os.system("cls")

# print("Bienvenidos a agenda 1.0")

# time.sleep(2)
# os.system("cls")

# Menú de opciones

opciones = {
    1: "Crear nuevo contacto",
    2: "Eliminar contacto",
    3: "Buscar contacto",
    4: "Ver todos los contactos",
    5: "Salir",
}

##############
def agregar_contato():
    print("contactos")



# Contactos

contactos = {}


def mostrar_diccionario(diccionario: dict):
    for x, y in diccionario.items():
        print(x, y)

def comprobar_eleccion(opcion):
    if opcion <= 5 and opcion >= 1:
        return False
    else:
        print("\n\nOpción erronea! \nPor favor elija una opción del 1 al 5\n")
        return True

def realizar_eleccion(opcion):
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    else:
        pass


valor = True

while valor:

    mostrar_diccionario(opciones)
    opcion_elegida = int(input("\nElija una opción: "))
    valor = comprobar_eleccion(opcion_elegida)