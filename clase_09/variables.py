from tkinter import Tk, StringVar, IntVar, DoubleVar, BooleanVar, Entry, Label
#Variables

# entero = IntVar() # Declara variable de tipo entera
# flotante = DoubleVar() # Declara variable de tipo flotante
# cadena = StringVar() # Declara variable de tipo cadena
# booleano = BooleanVar() # Declara variable de tipo booleana

ventana = Tk()
ventana.geometry('300x300')

nombre = StringVar()
id = IntVar()

nombre.set("Clase 9 (TKinter)")
id.set(1)

entrada = Entry(ventana, textvariable=nombre, width=25)
entrada.grid(row=0, column=0)
titulo = Label(ventana, textvariable=id)
titulo.grid(row=1, column=1)
ventana.mainloop()
