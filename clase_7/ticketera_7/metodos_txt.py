# Hacer que la ticketera cree un ticket nuevo al finalizar cada compra
# Poder eliminar un ticket cualquiera
# Ver todos los tickets
from datetime import datetime

class FechaHora:
    fecha_hora = datetime.now()

    def __init__(self):
        self.fecha = datetime.strftime(self.fecha_hora, "%d-%m-%Y")
        self.hora = datetime.strftime(self.fecha_hora, "%H:%M")


class TicketsTxt(FechaHora):

    def __init__(self, nombre, lista_productos):
        super().__init__()
        self.nombre = nombre
        self.lista_productos = lista_productos
        # self.total = total
    

    def crear_ticket(self):
        try:
            file = open(self.nombre, 'w')
            file.write(self.lista_productos + self.__str__())
            file.close()
        except:
            print("No se pudo crear el ticket...")
    


    def __str__(self):
        return f"\n\n{self.nombre[:-4]}\
                \n{self.hora}\
                \n{self.fecha}"

if __name__ == '__main__':
    ticket_1 = TicketsTxt("Ticket_1")
    print(ticket_1)