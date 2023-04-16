from tkinter import Label, Button, Entry, Frame, ttk, Tk, IntVar, StringVar, Toplevel
from model import Funciones as f
from view_aux import ComprobarDatos

##### PARA PROBAR LA APP EJECUTAR DESDE VIEW.PY ##################

window = Tk()

window.title("Python desde 0 Clase_10")  # Define el título de la ventana
window.geometry('400x500')  # Define las dimensiones de nuestra ventana
window.resizable(width=False, height=False) # Impide que se pueda modificar el alto y el ancho de la ventana

var_nombre = StringVar()
var_direccion = StringVar()
var_celular = IntVar()
var_celular.set('')

box_1 = Frame(window)
box_1.grid(row=0, column=0)

nombre = Label(box_1, text="Nombre")  # Definimos un título
# Por medio de grid realizamos una ubicación en grilla y (padx y pady) le damos un padding
nombre.grid(row=0, column=0, padx=5, pady=5)
# Generamos una entrada por medio de Entry
nombre_entry = Entry(box_1, textvariable=var_nombre)
# Ubicamos el entry al lado de su label correspondiente
nombre_entry.grid(row=0, column=1)

# Repetimos la acción
direccion = Label(box_1, text="Direccion")
direccion.grid(row=1, column=0, padx=5, pady=5)
direccion_entry = Entry(box_1, textvariable=var_direccion)
direccion_entry.grid(row=1, column=1)

#
celular = Label(box_1, text="Celular")
celular.grid(row=2, column=0, padx=5, pady=5)
celular_entry = Entry(box_1, textvariable=var_celular)
celular_entry.grid(row=2, column=1)


# BOTONES

guardar = Button(box_1, text='Guardar', width=10, command=lambda: funcion.guardar_datos((var_nombre.get(), var_direccion.get(), var_celular.get())))
guardar.grid(row=3, column=0, padx=20)

editar = Button(box_1, text='Editar', width=10, command=lambda: ComprobarDatos(tabla, funcion.dato_seleccionado()))
editar.grid(row=3, column=1, padx=20)

eliminar = Button(box_1, text='Eliminar', width=10, command=lambda: funcion.eliminar_datos("eliminar"))
eliminar.grid(row=3, column=2, padx=10)

# Tabla
box_2 = Frame(window, width=400, height=400, pady=10)
box_2.grid(row=4, column=0)


tabla = ttk.Treeview(box_2, columns=('col1', 'col2', 'col3'))
tabla.grid(row=0, column=0)
tabla.config(height=400)

tabla.column('#0', width=50)
tabla.column('col1', width=150)
tabla.column('col2', width=100)
tabla.column('col3', width=100)

tabla.heading('#0', text='ID')
tabla.heading('col1', text='NOMBRE')
tabla.heading('col2', text='DIRECCIÓN')
tabla.heading('col3', text='CELULAR')

funcion = f(tabla)



window.mainloop()