# from tkinter import *

# root = Tk()
# frame_1 = Frame(root, background='lightblue', pady=100, padx=100)
# frame_1.grid(row=1, column=0)

# frame_2 = Frame(root, bg='orange',pady=100, padx=100 )
# frame_2.grid(row=0, column=0)

# redbutton = Button(frame_1, text="Red", fg="red")
# redbutton.grid(row=0, column=0)

# greenbutton = Button(frame_1, text="Brown", fg="brown")
# greenbutton.grid(row=0, column=1)

# bluebutton = Button(frame_2, text="Blue", fg="blue", bg='lightgreen')
# bluebutton.grid(row=0, column=0)

# blackbutton = Button(frame_2, text="Black", fg="black", bg='lightgreen')
# blackbutton.grid(row=0, column=1)

# root.mainloop()

# from tkinter import *
  

# root = Tk()

# root.geometry("200x530")
  

# cursors =[
#         "arrow",
#         "circle",
#         "clock",
#         "cross",
#         "dotbox",
#         "exchange",
#         "fleur",
#         "heart",
#         "man",
#         "mouse",
#         "pirate",
#         "plus",
#         "shuttle",
#         "sizing",
#         "spider",
#         "spraycan",
#         "star",
#         "target",
#         "tcross",
#         "trek"
# ]
  
  

# for cursor in cursors:
#     Button(root,text=cursor,cursor=cursor).pack()
  
  
# root.mainloop()

# from tkinter import ttk, Tk

# window = Tk()

# treeview = ttk.Treeview(window, columns=('a1', 'a2'))
# treeview.grid(row=0, column=0)
# treeview.heading('#0',text='ID') # el método heading recibe como primer parametro el nombre de la columna y luego en la clave "text" debemos colocar el nombre que irá como cabecera
# treeview.heading('a1',text='Nombre')
# treeview.heading('a2',text='Apellido')

# treeview.column('#0',width=60, minwidth=50)
# treeview.column('a1',width=100, minwidth=70)
# treeview.column('a2',width=100, minwidth=70)

# treeview.insert('', 0, text='ID01', values=('Luis', 'Perez'))


# window.mainloop()

# from tkinter import *
# from tkinter import ttk


# def ventana_secundaria():
#     top = Toplevel()
#     top.geometry("300x100")
#     top.title("toplevel")
#     l2 = Label(top, text = "Esto es una ventana secundaria", font='Arial, 15')
#     l2.pack()
    
#     top.mainloop()


# ventana = Tk()
# ventana.title("Python desde 0")

# frame = Frame(ventana)
# frame.pack()

# treeview = ttk.Treeview(frame, columns=(2, 3), height=8)
# treeview.pack(side=LEFT)

# treeview.heading('#0', text="Nombre")
# treeview.heading(2, text="ID")
# treeview.heading(3, text="Salario")

# scroll = Scrollbar(frame, orient=VERTICAL)
# scroll.pack(side=RIGHT, fill=Y)

# treeview.config(yscrollcommand=scroll.set)
# scroll.config(command=treeview.yview)

# treeview.insert('', 0, text="vineet" ,values=("1", 1000000.00))
# treeview.insert('', 0, text="anil",  values=("2", 120000.00))
# treeview.insert('', 0, text="ankit", values=("3", 41000.00))
# treeview.insert('', 0, text="Shanti" ,values=("4", 22000.00))
# treeview.insert('', 0, text="vineet" ,values=("5", 1000000.00))
# treeview.insert('', 0, text="anil",  values=("6", 120000.00))
# treeview.insert('', 0, text="ankit", values=("7", 41000.00))
# treeview.insert('', 0, text="Shanti" ,values=("8", 22000.00))
# treeview.insert('', 0, text="vineet" ,values=("9", 1000000.00))
# treeview.insert('', 0, text="anil",  values=("10", 120000.00))
# treeview.insert('', 0, text="ankit", values=("11", 41000.00))
# treeview.insert('', 0, text="Shanti", values=("12", 22000.00))


# frame_2 = Frame(ventana, pady=10)
# frame_2.pack()

# boton_1 = Button(frame_2, text="Modificar", command=lambda: ventana_secundaria(), font='Arial, 12')
# boton_1.pack()


# ventana.mainloop()

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("200x200")
def hola_mundo():
   messagebox.showinfo("Decir hola", "Hola mundo")

B1 = Button(top, text = "Decir hola", command = hola_mundo)
B1.pack()

top.mainloop()