def mi_decorador(funcion):
    def envoltura():
        print("Código antes de ejecutar la función")
        funcion()
        print("Código despues de la función")
    return envoltura


@mi_decorador
def funcion_cualquiera():
    print("Código de otra función")


# funcion_cualquiera()


def decorador_con_params(funcion):
    def envoltura(*args, **kwargs):
        if sum(args)> 0:
            print('La suma es mayor a 0')
        resultado = funcion(*args, **kwargs)
        print("Código despues de la función")
        return resultado
    return envoltura


@decorador_con_params
def suma_de_numeros(*args):
    return sum(args)

print(suma_de_numeros(1, 2, 3))