from tkinter import *
from tkinter import ttk
# contador = 1
def capturar_datos(nom, ape, celu):
    tabla.insert('', 0, text=1, values=(nom, ape, celu))
    # contador = contador + 1


ventana_principal = Tk()
ventana_principal.geometry('703x450')
ventana_principal.title('Clase 10')

####################################### VARIABLES

nombre_entry = StringVar()
apellido_entry = StringVar()
celular_entry = IntVar()

# ###################################### ENTRADAS

caja_entradas = Frame(ventana_principal, padx=20)
caja_entradas.grid(row=0, column=0)

titulo_nombre = Label(caja_entradas, text='Nombre', font='Arial 22', padx=20, pady=10)
titulo_nombre.grid(row=0, column=0)

titulo_apellido = Label(caja_entradas, text='Apellido', font='Arial 22', padx=20, pady=10)
titulo_apellido.grid(row=1, column=0)

titulo_celular = Label(caja_entradas, text='Celular', font='Arial 22', padx=20, pady=10)
titulo_celular.grid(row=2, column=0)

entrada_nombre = Entry(caja_entradas, font='Arial 22', textvariable=nombre_entry)
entrada_nombre.grid(row=0, column=1)

entrada_apellido = Entry(caja_entradas, font='Arial 22', textvariable=apellido_entry)
entrada_apellido.grid(row=1, column=1)

entrada_cel = Entry(caja_entradas, font='Arial 22', textvariable=celular_entry)
entrada_cel.grid(row=2, column=1)

# ################################# BOTONES

caja_botones = Frame(ventana_principal, padx=10)
caja_botones.grid(row=0, column=1)

boton_agregar = Button(caja_botones, 
                       text='Agregar', 
                       font='Arial 18', 
                       width=10,
                       command=lambda: capturar_datos(nombre_entry.get(),
                                                      apellido_entry.get(),
                                                       celular_entry.get() ))
boton_agregar.grid(row=0, column=0, pady=10)

boton_editar = Button(caja_botones, text='Editar', font='Arial 18', width=10)
boton_editar.grid(row=1, column=0, pady=10)

boton_eliminar = Button(caja_botones, 
                        text='Eliminar', 
                        font='Arial 18', 
                        width=10,
                        command=lambda: print("Eliminar"))
boton_eliminar.grid(row=2, column=0, pady=10)

caja_tabla = Frame(ventana_principal, bg='orange')
caja_tabla.grid(row=1, column=0, columnspan=2)

# tabla = Label(caja_tabla, text='TABLA', font='Arial 30')
# tabla.grid(row=0, column=0)

tabla = ttk.Treeview(caja_tabla, columns=('col1', 'col2', 'col3'))
tabla.grid(row=0, column=0)

tabla.heading('#0', text='ID')
tabla.heading('col1', text='Nombre')
tabla.heading('col2', text='Apellido')
tabla.heading('col3', text='Celular')

tabla.column('#0', width=100)



ventana_principal.mainloop()