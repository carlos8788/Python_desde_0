from tkinter import *
top = Tk()
check_var = IntVar()
check_var_2 = IntVar()
C1 = Checkbutton(top, text = "Valor 1", variable = check_var,
onvalue = 1, offvalue = 0,
command=lambda: print("valor C1:", check_var.get()))
C1.config(height=5, width = 20)
C2 = Checkbutton(top, text = "Valor 2", variable = check_var_2,
onvalue = 1, offvalue = 0,
command=lambda: print("valor C2:", check_var_2.get()))
C2.config(height=5, width = 20)
C1.pack()
C2.pack()
top.mainloop()