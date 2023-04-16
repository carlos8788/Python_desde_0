# Pedirle al usuario que ingrese 2 número enteros y que devuelva la suma, la multiplicación
# la resta y division

# una pequeña ayuda
numero_a = int(input("Ingrese un número entero: "))
numero_b = int(input("Ingrese un número entero: "))

suma = int(numero_a + numero_b)
multiplicacion = int(numero_a * numero_b)
resta = int(numero_a - numero_b)
division = round((numero_a / numero_b),2)


print(
    f'Los resultados son:\n suma:{suma} \n multiplicación:{multiplicacion}\n resta:{resta}\n division:{division}')