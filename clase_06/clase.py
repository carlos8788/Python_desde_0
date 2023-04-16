class Planta:
    def __init__(self, nombre: str, flores: bool, ambiente: str):
        self.flores = flores
        self.nombre = nombre
        self.ambiente = ambiente

class Tallo(Planta):
    def __init__(self, tallo: str, nombre: str, flores: bool, ambiente: str):
        super().__init__(nombre, flores, ambiente)
        self.tallo = tallo
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nFlores: {self.flores}\nTallo: {self.tallo}"

malvon = Tallo("Fino", "Malvon", True, "Exterior")
print(malvon) # <__main__.Tallo object at 0x000001F06E16BBB0>


