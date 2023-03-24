class Persona:
    def __init__(self, edad, nombre, apellido):
        self.edad = edad
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar_persona(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}"



  