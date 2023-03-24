nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = int(input("Ingresá tu edad: ")
           )
anio_nacimiento = 2023 - edad

es_mayor = 18 <= edad


print(f'Su nombre es: {nombre}')
print(f"Su apellido es: {apellido}")
print(f"Su edad es: {edad}")
print(f"Su año de nacimiento es: {anio_nacimiento}")
print(f"Es mayor?: {es_mayor}")

# Ejercicio 2
# Pedirle al usuario que ingrese 2 número enteros y que devuelva la suma, la multiplicación
# la resta y division

numero_a = int(input("Ingrese un número entero: "))
numero_b = int(input("Ingrese otro número entero: "))

suma = numero_a + numero_b
resta = numero_a - numero_b
multiplicacion = numero_a * numero_b
division = numero_a / numero_b

print(suma)
print(resta)
print(multiplicacion)
print(division)

nombre = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")
edad = int(input("Edad: "))
