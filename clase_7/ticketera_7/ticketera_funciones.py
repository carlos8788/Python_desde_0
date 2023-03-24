from metodos_txt import TicketsTxt
import sistema
lista_productos={}

def agregar_producto(diccionario: dict):
    nombre = input("Ingrese el nombre del producto: ")
    if nombre in diccionario:
        print("Este producto ya existe, intente con otro.")
    else:    
        
        cantidad = input("Ingrese la cantidad: ")
        precio = input("Ingrese el precio: ")

        diccionario[nombre] = {'Cantidad': cantidad, 'Precio': precio}

        print("Producto guardado.\n")

def eliminar_producto(diccionario: dict):

    nombre = input("Ingrese el nombre del producto que quiera eliminar: ")
    if nombre in diccionario:
        diccionario.pop(nombre)
    else:
        print("El nombre ingresado no está en la lista de productos\n")

    print(f"Producto {nombre} eliminado")



def ver_productos(diccionario: dict):
    cadena = ''
    for clave,valor in diccionario.items():
        print(f"\n{clave}:")
        cadena += f"\n{clave}:\n"
        for a, b in valor.items():
            print(f"\t{a}: {b}")
            cadena += f"\t{a}: {b}"
    return (cadena+'\n')
    

def sumar_todo(diccionario: dict):    
    suma_total = 0
    suma_cantidad = 0
    cadena = ''
    for valor in diccionario.values():
        lista_2 = []
        for b in valor.values():
            lista_2.append(b)
        suma_total = suma_total + (int(lista_2[0]) * float(lista_2[1]))
        suma_cantidad = suma_cantidad + int(lista_2[0])
    print(f"Cantidad total: {suma_cantidad}\nTotal: ${suma_total}")
    cadena += f"Cantidad total: {suma_cantidad}\nTotal: ${suma_total}"
    return cadena

def mostrar_diccionario(diccionario: dict):
    for x,y in diccionario.items():
        print(f"{x}. {y}")

def comprobar_ticket(nombre, lista):
    contador = 0
    while nombre in lista:
        contador += 1
        nombre = 'ticket_' + str(contador) + '.txt'
    return nombre

def crear_obj_ticket(productos, total):
    cadena = productos + '\n' + total
    contador = 0
    lista = sistema.mostrar_tickets()
    nombre = 'ticket_'+ str(contador) + '.txt'
    
    if not nombre in lista:
        ticket = TicketsTxt(nombre, cadena)
        ticket.crear_ticket()
    else:
        nombre_2 = comprobar_ticket(nombre, lista)
        ticket = TicketsTxt(nombre_2, cadena)
        ticket.crear_ticket()

    


def comprobar_opcion(opcion):

    if opcion >= 1 and opcion <= 6:
        if opcion == 1:
            agregar_producto(lista_productos)
            return False
        
        elif opcion == 2:
            eliminar_producto(lista_productos)
            return False
        
        elif opcion == 3:
            ver_productos(lista_productos)
            return False
        
        elif opcion == 4:
            print("***"*10,'\n')
            for i in sistema.mostrar_tickets():
                if 'ticket' in i:
                    
                    print(i)
            print('\n')
            print("***"*10,'\n')
            return False
        
        elif opcion == 5:
            nombre_ticket = input("Ingrese el ticket que desea eliminar: ")
            sistema.eliminar_ticket(nombre_ticket)
            return False

        elif opcion == 6:
            print("\n")
        
            total = sumar_todo(lista_productos)
            productos = ver_productos(lista_productos)
            crear_obj_ticket(productos, total)
            return True


        return True

    else:
        print("\n Opción incorrecta, por favor elija una del 1 al 6\n")
        return False