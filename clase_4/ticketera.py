import ticketera_funciones as tick


menu = {
    1: "Agregar producto",
    2: "Eliminar producto",
    3: "Ver lista de productos",
    4: "Finalizar compra"
}

menu_variable = False

while not menu_variable:
    tick.mostrar_diccionario(menu)

    valor = int(input("\nElija una opción: "))

    menu_variable = tick.comprobar_opcion(valor)