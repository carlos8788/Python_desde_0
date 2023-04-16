class Estudiante:
    def __init__(self, edad, nombre, apellido):
        self.edad = edad
        self.nombre = nombre
        self.apellido = apellido

class Instituto:
    def __init__(self, nombre_instituto):
        self.nombre_instituto = nombre_instituto

class Carrera(Estudiante, Instituto):
    def __init__(self, edad, nombre, apellido, nombre_instituto, nombre_carrera):
        Estudiante.__init__(self, edad, nombre, apellido)
        Instituto.__init__(self, nombre_instituto)
        self.nombre_carrera = nombre_carrera
    

# alumno = Carrera(34, "Luis", "Perez", "CoderOffice", "Informática")
# print(type(alumno)) #<class '__main__.Carrera'>

class Clase0:
    def __init__(self, atr0):
        self.atr0 = atr0
    def __str__(self):
        return f"Esta es la Clase0 {self.atr0}"

class Clase1:
    def __init__(self, atr1):
        self.atr1 = atr1

class Clase2:
    def __init__(self, atr2):
        self.atr2 = atr2

class Clase3(Clase1, Clase2):
    def __init__(self, atr1, atr2, atr3):
        Clase1.__init__(self, atr1)
        Clase2.__init__(self, atr2)
        self.atr3 = atr3

        self.clase_0 = Clase0("Instanciada desde la CLase3")
        # print(self.clase_0)

ejemplo_clases = Clase3("atributo 1", "atributo 2", "atributo 3")
# Esta es la Clase0 La clase 0