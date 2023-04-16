from datetime import datetime

fecha_hora = datetime.now()
print(fecha_hora)

fecha_formateada = datetime.strftime(fecha_hora, "%d-%m-%Y / %H.%M")

print(fecha_formateada)