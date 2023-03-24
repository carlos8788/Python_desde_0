from tkinter import Tk, Label, Button, Entry, EW
from tkinter import StringVar, IntVar, DoubleVar, BooleanVar


def imprimir():
    widget_label_2.config(text=widget_entry.get())

ventana = Tk()

entero = IntVar() # Declara variable de tipo entera
flotante = DoubleVar() # Declara variable de tipo flotante
cadena = StringVar(value="Python desde 0") # Declara variable de tipo cadena
booleano = BooleanVar() # Declara variable de tipo booleana

#Edicion de la ventana
ventana.title('App Python Tkinter') # Nos permite colocar un título
ventana.iconbitmap('python.ico') # Colocar un ícono
ventana.geometry('300x300') # El ancho y alto de la ventana al iniciar
ventana.config(background='gray') # Cambiar configuraciones del
# objeto ventana, en este caso el fondo con el parametro background

widget_label = Label(ventana, text='Titulo', padx=50, background='#90EC73')
widget_label.grid(row=0, column=0, padx=5, pady=5)
widget_entry = Entry(ventana)
widget_entry.grid(row=0, column=1, padx=8, pady=5)
widget_button = Button(ventana, text='Modificar título', command=imprimir)
widget_button.grid(row=2, column=0, columnspan=2, pady=5,sticky=EW)

widget_label_2 = Label(ventana, text='', padx=50, background='#AFE5EE')
widget_label_2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()