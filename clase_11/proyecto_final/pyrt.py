numero = 0
n = 101
while n != 0:
        numero = 10*numero+n % 10
        n //= 10
print(n)
print(numero == n)

# numero = 0
# capicua = 101
# capicua = int(capicua)
# while capicua != 0:
#   numero = 10 * numero + capicua % 10
#   capicua = int(capicua / 10)
#   print(capicua)
# print('Es capicua?')
# print(capicua == numero)