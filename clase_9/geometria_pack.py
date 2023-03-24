from tkinter import Tk, Button

ventana = Tk()
redbutton = Button(ventana, text="Red", fg="red") # fg : cambia el color de la letra
redbutton.config(padx=100)
redbutton.pack()
greenbutton = Button(ventana, text="green", fg="green")
greenbutton.config(padx=100)
greenbutton.pack()
bluebutton = Button(ventana, text="Blue", fg="blue")
bluebutton.config(padx=100)
bluebutton.pack()
blackbutton = Button(ventana, text="Black", fg="black")
blackbutton.config(padx=100)
blackbutton.pack()

ventana.mainloop()