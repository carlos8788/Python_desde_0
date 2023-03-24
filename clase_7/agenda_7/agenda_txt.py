class Txt:
    def __init__(self, nombre):
        self.nombre = nombre
        self.file = open(self.nombre, 'a')
        self.file.close()

    def agregar_contactos(self, contactos: dict):
        string = ""
        for i,j in contactos.items():
            string = string + i + ","
            for x in j.values():
                string = string + x + ","
            string = string[:-2] + '\n'

        self.file = open(self.nombre, 'w')
        self.file.write(string)
        self.file.close()
    
    def obtener_contactos(self):
        diccionario ={}
        self.file = open(self.nombre, 'r')
        for obtener_contactos in self.file:
            lista_temp = obtener_contactos.split(",")
            lista_temp[3] = lista_temp[3][:-1]
            diccionario[lista_temp[0]] = { "ID": lista_temp[1], 'Direccion': lista_temp[2], 'Celular': lista_temp[3]}
        return diccionario
            
        
    
        
if __name__ == '__main__':
    agenda = Txt("agenda.txt")
    print(agenda.obtener_contactos())

    # tupla = "123456789"
    # print(list(tupla))