from tkinter import Tk, Label, Button, Entry



def imprimir():
    widget_label_2.config(text=widget_entry.get())


# Ventana principal
ventana = Tk()

ventana.title('App Python Tkinter') 

ventana.iconbitmap('python.ico') 

ventana.geometry('300x300') 

ventana.config(background='#AFE5EE') 



# Widgets
widget_label = Label(ventana, text='Titulo', padx=50, background='#90EC73')
widget_label.grid(row=0, column=0, padx=5, pady=5)

widget_entry = Entry(ventana)
widget_entry.grid(row=0, column=1, padx=8)

widget_button = Button(ventana, text='Modificar título', command=imprimir)
widget_button.grid(row=1, column=0, columnspan=2, sticky='EW')

widget_label_2 = Label(ventana, text='', padx=50, background='#AFE5EE')
widget_label_2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)



ventana.mainloop()