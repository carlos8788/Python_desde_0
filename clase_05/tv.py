import random
import time
import os

class Tv:

    def __init__(self, modelo, marca, cant_canales, pulgadas, precio):
        self.modelo = modelo
        self.marca = marca
        self.cant_canales = cant_canales
        self.pulgadas = pulgadas
        self.precio = precio
        self.encendido = False
        self.volumen_tv = 1
        self.canal = random.randint(1, self.cant_canales)

    def __str__(self):
        return f" \
                Modelo: {self.modelo}\n \
                Marca: {self.marca}\n \
                Canales: {self.cant_canales}\n \
                Pulgadas: {self.pulgadas}\n \
                Precio: ${self.precio}"

    def encender(self):
        time.sleep(3)
        if self.encendido == False:
            self.encendido = True
            print("La tv está encendida")  
            return self.encendido
        else:
            self.encendido = False
            print("La tv está apagada")
            return self.encendido  

    def cambiar_canal(self, canal_elegido):
        print(f"Canal actual: {self.canal}")
        
        if canal_elegido <= self.cant_canales and canal_elegido > 0:
            if self.canal == canal_elegido:
                return "No se puede cambiar el canal porque es el mismo"
            else:
                self.canal = canal_elegido
                return f"Canal actual: {self.canal}"
        else:
            return f"El canal {canal_elegido} elegido no existe"

    def subir_volumen(self):
        time.sleep(0.5)
        if self.volumen_tv == 50:
            return "El volumen está al máximo"
        else:
            self.volumen_tv += 1
            return f"Subiendo Volumen: {self.volumen_tv}"


    def bajar_volumen(self):
        time.sleep(0.5)
        if self.volumen_tv == 0:
            return "El volumen está al mínimo"
        else:
            self.volumen_tv -= 1
            return f"Bajando Volumen: {self.volumen_tv}"

print("**********")
print(f"La variable __name__ es:{__name__}", "\n")
if __name__ == "__main__":

    # os.system('cls')

    philco = Tv("RT24", "Philco", 4, "24", 35000)

    print(philco)
    # philco.encender()
    # philco.encender()
    print(philco.cambiar_canal(0))
    print(philco.cambiar_canal(4))
    print(philco.cambiar_canal(3))
    print(philco.cambiar_canal(5))

    # print(philco.subir_volumen())

    # print(philco.subir_volumen())

    # print(philco.bajar_volumen())

    # print(philco.bajar_volumen())

    # print(philco.bajar_volumen())

    # print(philco.bajar_volumen())

    # print(philco.bajar_volumen())

