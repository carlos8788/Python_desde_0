from agenda_txt import Txt

agenda = Txt('agenda.txt')
contactos = agenda.obtener_contactos()

def mostrar_diccionario(diccionario: dict):
    for x, y in diccionario.items():
        print(f"{x}. {y}")


def agregar_contacto():

    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in contactos:
        print("Este contacto ya existe, intente con otro.")
    else:
        id = input("Ingrese el ID: ")
        direccion = input("Ingrese la dirección: ")
        celular = input("Ingrese el celular: ")

        contactos[nombre] = {
            "ID": id, 'Direccion': direccion, 'Celular': celular}

        print("Contacto guardado.\n")


def eliminar_contacto():

    nombre = input("Ingrese el nombre del contacto que quiera eliminar: ")
    if nombre in contactos:
        contactos.pop(nombre)
    else:
        print("El nombre ingresado no está en la lista de contactos\n")

    print(f"Contacto {nombre} eliminado")


def editar_contacto():

    nombre = input("Ingrese el nombre del contacto que quiera editar: ")
    if nombre in contactos:
        contacto = contactos[nombre]
        direccion = input("Introduzca la nueva dirección: ")
        celular = input("Introduzca el celular: ")
        contacto.update({'Direccion': direccion, 'Celular': celular})
        print("Actualización realizada")
    else:
        print("\nEl contacto no existe. \n\n")


def ver_contactos():
    for clave, valor in contactos.items():
        print(f"\n{clave}:")
        for a, b in valor.items():
            print(f"\t{a}: {b}")
    


def buscar_contacto():
    nombre = input("Introduzca un nombre a buscar: ")
    if nombre in contactos:
        print(f"\n{nombre.upper()}:\n")

        contacto = contactos[nombre]

        for x, y in contacto.items():
            print(f"{x}: {y}")
    else:
        print("Contacto no encontrado")
    print("\n")


def comprobar_opcion(opcion):
    if opcion >= 1 and opcion <= 6:
        if opcion == 1:
            agregar_contacto()
            return True
        elif opcion == 2:
            eliminar_contacto()
            return True
        elif opcion == 3:
            editar_contacto()
            return True
        elif opcion == 4:
            ver_contactos()
            print("\n")
            return True
        elif opcion == 5:
            buscar_contacto()
            return True

        elif opcion == 6:
            agenda.agregar_contactos(contactos)
            return False

        return True

    else:
        print("\n Opción incorrecta, por favor elija una del 1 al 6\n")
        return True
