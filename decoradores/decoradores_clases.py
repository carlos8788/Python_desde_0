def verificar_encendido(cls):
    class Envoltura:
        def __init__(self, *args, **kwargs):
            self.instancia_original = cls(*args, **kwargs)

        def encender(self):
            self.instancia_original.encendido = True
            print("El auto ha sido encendido.")

        def apagar(self):
            self.instancia_original.encendido = False
            print("El auto ha sido apagado.")

        def __getattr__(self, nombre):
            attr = getattr(self.instancia_original, nombre)

            if callable(attr):
                def envoltura(*args, **kwargs):
                    if getattr(self.instancia_original, "encendido", False):
                        return attr(*args, **kwargs)
                    else:
                        print(f"El auto debe estar encendido para ejecutar {nombre}.")
                return envoltura
            else:
                return attr

    return Envoltura

@verificar_encendido
class Automovil:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False

    def conducir(self):
        print("Conduciendo el auto. ")

    def tocar_bocina(self):
        print("Tocando la bocina.")

auto = Automovil('fiat')

auto.conducir()  # Salida: El auto debe estar encendido para ejecutar conducir.
auto.encender()  # Salida: El auto ha sido encendido.
auto.conducir()  # Salida: Conduciendo el auto.
auto.tocar_bocina()  # Salida: Tocando la bocina.
auto.apagar()  # Salida: El auto ha sido apagado.
auto.conducir()  # Salida: El auto debe estar encendido para ejecutar conducir.


# def mi_decorador(cls):
#     def mi_decorador(cls):
#         cls.atributo_adicional = "valor adicional"
#         return cls

# @mi_decorador
# class MiClase:
#     pass    


# class MiDecorador:
#     def __init__(self, funcion):
#         self.funcion = funcion

#     def __call__(self, *args, **kwargs):
#         print("Código antes de la función original")
#         self.funcion(*args, **kwargs)
#         print("Código después de la función original")

# @MiDecorador
# def saludo(nombre):
#     print(f"¡Hola, {nombre}!")

def mi_decorador(funcion):
    class Envoltura:
        def __init__(self, *args, **kwargs):
            self.funcion = funcion
            self.args = args
            self.kwargs = kwargs

        def __call__(self):
            print("Código antes de la función original")
            self.funcion(*self.args, **self.kwargs)
            print("Código después de la función original")

    return Envoltura

@mi_decorador
def saludo(nombre):
    print(f"¡Hola, {nombre}!")

print(type(saludo())) # <class '__main__.mi_decorador.<locals>.Envoltura'>
saludo_decorado = saludo("mundo")
saludo_decorado() # con esto conseguimos que se ejecute el método __call__


