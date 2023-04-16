class Automovil:
    
    def __init__(self, modelo, color, puertas, combustible, cambio, precio):
        self.modelo = modelo
        self.color = color
        self.puertas = puertas
        self.combustible = combustible
        self.cambio = cambio
        self.precio = precio
        self.litros_combustible = 0
        self.en_marcha = False


    def __str__(self):
            return f" \
                Modelo: {self.modelo}\n\
                 Color: {self.color}\n \
                Puertas: {self.puertas}\n \
                Combustible: {self.combustible}\n \
                Caja de cambios: {self.cambio}\n \
                Precio: ${self.precio}"


    def consultar_cantidad_combustible(self):
        print(f"Litros de combustible: {self.litros_combustible}")
        

    def cargar_combustible(self, litros: float):
        self.litros_combustible += litros
        print(f"Se cargaron {litros} litros de {self.combustible}\n\
        Total: {self.litros_combustible}")
        return self.litros_combustible


    def encendido(self):
        if self.en_marcha == False:
            self.en_marcha = True
            print("El auto está en marcha")
            return self.en_marcha
        else:
            self.en_marcha = False
            print("El auto está apagado")
            return self.en_marcha


if __name__ == "__main__":
    auto = Automovil("Ford ka", "Azul", "5", "Nafta", "manual", 2000000)
    auto.encendido()
    print(auto)
    auto.encendido()
    