import subprocess
import time
time_ = int(input("Ingresa el tiempo que desees en minutos: "))
time_ = time_ * 60
subprocess.run(f'shutdown -s -t {time_}')

# tiempo = 60
# while tiempo >= 0:
#     print(tiempo)
#     time.sleep(1)
#     tiempo -= 1

# mi_lista = [1, 2, 3, 4, 5]

# # for i in mi_lista:
# #     print(i)

# contador = 4

# while contador < 10:
#     print(contador)
#     print("Estoy en el ciclo while")
#     contador = contador + 1

# diccionario = dict(pedro=(dict(edad=22, altura=187))) 
# print(diccionario) # {'pedro': {'edad': 22, 'altura': 187}}
