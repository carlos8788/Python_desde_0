from tkinter import *
from tkinter import messagebox

def capturar_datos(tabla, nom, ape, celu):
    tabla.insert('', 0, text=1, values=(nom.get(), ape.get(), celu.get()))
    nom.set('')
    ape.set('')
    celu.set('')

    
def vista_secu(tabla, nom: str, ape: str, celu:int):
   
    window_2 = Toplevel()
    window_2.geometry('400x600')

    nombre_ent = StringVar()
    ape_ent = StringVar()
    celu_ent = IntVar()

    nombre_ent.set(nom)
    ape_ent.set(ape)
    celu_ent.set(celu)

    nombre_tit = Label(window_2, text="Nombre", font='Arial 20')
    nombre_tit.grid(row=0, column=0)

    apellido_tit = Label(window_2, text="Apellido", font='Arial 20')
    apellido_tit.grid(row=1, column=0)

    celu_tit = Label(window_2, text="Celular", font='Arial 20')
    celu_tit.grid(row=2, column=0)

    entrada_nombre = Entry(window_2, font='Arial 20', textvariable=nombre_ent)
    entrada_nombre.grid(row=0, column=1)

    entrada_apellido = Entry(window_2, font='Arial 20', textvariable=ape_ent)
    entrada_apellido.grid(row=1, column=1)

    entrada_celular = Entry(window_2, font='Arial 20', textvariable=celu_ent)
    entrada_celular.grid(row=2, column=1)

    boton_guardar = Button(window_2, text="Guardar", font='Arial 20', width=10 ,command=lambda: capturar_datos(tabla,
                                                                                                               nombre_ent,
                                                                                                                ape_ent,
                                                                                                                celu_ent ))
    boton_guardar.grid(row=3, column=0, padx=5, pady=5)
    boton_cancel = Button(window_2, text="Cancelar", font='Arial 20', width=10 ,command=lambda: window_2.destroy())
    boton_cancel.grid(row=3, column=1, padx=5, pady=5)
    window_2.mainloop()


def editar_datos(tabla):
    item = tabla.focus()
    data = tabla.item(item)
    lista_datos = data['values']
    if(type(lista_datos[0])) is str and (type(lista_datos[1])) is str and (type(lista_datos[2])) is int:
        vista_secu(tabla, lista_datos[0], lista_datos[1], lista_datos[2])
    else:
        messagebox.showerror('Error', 'No se pasaron datos correctos')
    
    


    

# func_anonima = lambda x,y: print(f"Lambda {x + y}")

# func_anonima(10, 90)