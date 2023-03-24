import os
def mostrar_tickets():
    lista = []
    # os.system("cls")
    # print(f"Ruta: {os.getcwd()}")
    # print(os.listdir())
    for elementos in os.listdir():
        if elementos.endswith('.txt'):
            lista.append(elementos)
    return lista

def eliminar_ticket(nombre_ticket):
    
    try:
        os.remove(nombre_ticket)
        print("Ticket eliminado")
            
    except FileNotFoundError:
        print("No se pudo encontrar el ticket")
            
    

if __name__ == '__main__':
    lista = mostrar_tickets()
    print(not 'ticket0.txt' in lista)