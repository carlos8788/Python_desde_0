from persona import Persona

class Estudiante(Persona):
    def __init__(self, edad, nombre, apellido, carrera, turno):
        super().__init__(edad, nombre, apellido)
        self.carrera = carrera
        self.turno = turno

