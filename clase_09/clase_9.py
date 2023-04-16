from tkinter import Tk, Label, Entry, Button,EW
from tkinter import StringVar, IntVar, DoubleVar, BooleanVar

# def imprimir():
#     widget_label_2.config(text=widget_entry.get())

# ventana = Tk()

# ventana.title('App Python Tkinter') 

# ventana.iconbitmap('python.ico') 

# ventana.geometry('300x300') 
# 

# ventana.config(background='#AFE5EE') 

# widget_label = Label(ventana, text='Titulo', padx=50, background='#90EC73')
# widget_label.grid(row=0, column=0, padx=5, pady=5)

# widget_entry = Entry(ventana)
# widget_entry.grid(row=0, column=1, padx=8)

# widget_button = Button(ventana, text='Modificar título', command=imprimir)
# widget_button.grid(row=1, column=0, columnspan=2, sticky=EW)

# widget_label_2 = Label(ventana, text='', padx=50, background='#AFE5EE')
# widget_label_2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# ventana.mainloop()

# entero = IntVar()  # Declara variable de tipo entera
# flotante = DoubleVar()  # Declara variable de tipo flotante
# cadena = StringVar()  # Declara variable de tipo cadena
# booleano = BooleanVar()  # Declara variable de tipo booleana

# cadena = StringVar(value="Python desde 0")


# ventana = Tk()
# ventana.geometry('300x300') 
# nombre = StringVar()

# id = IntVar()

# nombre.set("Clase 9 (TKinter)")
# id.set(1)

# entrada = Entry(ventana, textvariable=nombre, width=25)
# entrada.grid(row=0, column=0)
# titulo = Label(ventana, textvariable=id)
# titulo.grid(row=1, column=1)
# ventana.mainloop()

# nombre.get() # Clase 9 (TKinter)
# id.get() # 1


# from tkinter import *

# ventana = Tk()


# redbutton = Button(ventana, text="Red", fg="red") # fg : cambia el color de la letra
# redbutton.config(padx=100)
# redbutton.pack()


# greenbutton = Button(ventana, text="green", fg="green")
# greenbutton.config(padx=100)
# greenbutton.pack()

# bluebutton = Button(ventana, text="Blue", fg="blue")
# bluebutton.config(padx=100)
# bluebutton.pack()

# blackbutton = Button(ventana, text="Black", fg="black")
# blackbutton.config(padx=100)
# blackbutton.pack()

# ventana.mainloop()


# from tkinter import *

# def sel():
#    seleccion = "Eligió Opción " + str(var.get())
#    label.config(text = seleccion)

# ventana = Tk()
# var = IntVar()
# boton1 = Radiobutton(ventana, text="Opción 1", variable=var, value=1,
#                   command=sel)
# boton1.pack( anchor = W )

# boton2 = Radiobutton(ventana, text="Opción 2", variable=var, value=2,
#                   command=sel)
# boton2.pack( anchor = W )

# boton3 = Radiobutton(ventana, text="Opción 3", variable=var, value=3,
#                   command=sel)
# boton3.pack( anchor = W)

# label = Label(ventana)
# label.pack()
# ventana.mainloop()

# from tkinter import PhotoImage


# icono_grande = PhotoImage(file="python.png")
# ventana.iconphoto(False, icono_grande)