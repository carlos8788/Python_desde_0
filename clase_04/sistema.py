import os

os.system("cls")
print(f"Ruta: {os.getcwd()}")
print(os.listdir())

for elementos in os.listdir():
    if elementos.endswith('.py'):
        print(elementos)
