"""
Para este ejercicio se pide que completes y corrijas el código para que funcione
Deberás mostrar en la consola 
Nombre
Apellido
Edad
Año de nacimiento
Si es mayor de edad
"""

# Entrada de datos:

nombre = input("Ingresá tu nombre: ")
apellido = input('Ingrese su apellido: ')
edad = int(input("Edad: "))

# Procesando los datos:

anio_nacimiento =  2022 - edad

es_mayor = 18 < edad

# Salida de datos

print(f'Su nombre es: {nombre}')
print(f"Su apellido es: {apellido}")
print(f"Su edad es: {edad}")
print(f"Su año de nacimiento es: {anio_nacimiento}")

print(f'Hola {nombre} {apellido}, tu edad indica que naciste en el año {anio_nacimiento}')
print(f'{nombre} es mayor de edad?:{es_mayor}')