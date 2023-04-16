from tkinter import *
from tkinter import ttk

from modelo import *






# ##################### VISTA #################################

ventana_principal = Tk()
ventana_principal.geometry('703x450')
ventana_principal.title('Clase 11')

####################################### VARIABLES

nombre_entry = StringVar()
apellido_entry = StringVar()
celular_entry = IntVar()

celular_entry.set('')
#
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
                       command=lambda: capturar_datos(tabla,nombre_entry,
                                                      apellido_entry,
                                                       celular_entry ))
boton_agregar.grid(row=0, column=0, pady=10)

boton_editar = Button(caja_botones, text='Editar', font='Arial 18', width=10,
                            command=lambda: editar_datos(tabla))
boton_editar.grid(row=1, column=0, pady=10)

boton_eliminar = Button(caja_botones, 
                        text='Eliminar', 
                        font='Arial 18', 
                        width=10,
                        command=lambda: print("Eliminar"))
boton_eliminar.grid(row=2, column=0, pady=10)


# ################################# TABLA

caja_tabla = Frame(ventana_principal)
caja_tabla.grid(row=1, column=0, columnspan=2)


tabla = ttk.Treeview(caja_tabla, columns=('col1', 'col2', 'col3'), name='tabla')
tabla.grid(row=0, column=0)


tabla.heading('#0', text='ID')
tabla.heading('col1', text='Nombre')
tabla.heading('col2', text='Apellido')
tabla.heading('col3', text='Celular')

tabla.column('#0', width=100)

style = ttk.Style()
# style.theme_use('winnative')
style.configure('Treeview',
                font='Arial 18',
                rowheight=35,
                )
style.configure("Treeview.Heading", font='None 18 italic', foreground='red')


# ################################# MENÚ 

# def archivo_nuevo_presionado():
#     print("¡Has presionado para crear un nuevo archivo!")

# barra_menu = Menu()

# menu_archivo = Menu(barra_menu, tearoff=False, font='Arial 14')
# menu_archivo.add_command(
#     label="Nuevo",
#     # accelerator="Ctrl+N",
#     command=archivo_nuevo_presionado
# )
# barra_menu.add_cascade(menu=menu_archivo, label="Archivo")

# ventana_principal.config(menu=barra_menu)


def imprimir():
   print("Operando en el menú")
   

menubar = Menu(ventana_principal)

filemenu = Menu(menubar, tearoff=False, font='Arial 14')

menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Archivo", command=imprimir)
filemenu.add_command(label="Editar", command=imprimir)
filemenu.add_command(label="Guardar", command=imprimir)
filemenu.add_command(label="Guardar como...", command=imprimir)

filemenu.add_separator()

filemenu.add_command(label="Salir", command=lambda : ventana_principal.destroy())




editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label="Deshacer", command=imprimir)

editmenu.add_separator()

editmenu.add_command(label="Cortar", command=imprimir)
editmenu.add_command(label="Copiar", command=imprimir)
editmenu.add_command(label="Pegar", command=imprimir)

menubar.add_cascade(label="Editar", menu=editmenu)

helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label="Ayuda", command=imprimir)
helpmenu.add_command(label="Acerca de...", command=imprimir)


menubar.add_cascade(label="Ayuda", menu=helpmenu)

ventana_principal.config(menu=menubar)



ventana_principal.mainloop()

