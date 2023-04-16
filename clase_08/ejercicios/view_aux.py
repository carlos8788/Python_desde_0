from tkinter import Toplevel, Label, Button, Entry, StringVar, IntVar
from model import Funciones

##### PARA PROBAR LA APP EJECUTAR DESDE VIEW.PY ##################

class ComprobarDatos:
    def __init__(self, tabla, datos):

        self.tabla = tabla
        self.datos = datos
        self.funcion = Funciones(tabla)
        
        self.comprobar()
        

    def comprobar(self):
        if self.funcion.comprobar_contacto(self.datos, "editar"):
            return VentanaSecundaria(self.tabla, self.datos)



class VentanaSecundaria:
    def __init__(self, tabla, datos):
        self.funcion = Funciones(tabla)
        # print(datos)
        self.sec_var_nombre = StringVar()
        self.sec_var_direccion = StringVar()
        self.sec_var_celular = IntVar()
        
        self.funcion.rellenar_campos(
            (self.sec_var_nombre,
            self.sec_var_direccion,
            self.sec_var_celular),
            datos
        )

        self.window_2 = Toplevel()

        self.window_2.title("Secundaria")  # Define el título de la ventana
        self.window_2.geometry('300x200')  # Define las dimensiones de nuestra ventana
        self.window_2.resizable(width=False, height=False) # Impide que se pueda modificar el alto y el ancho de la ventana

        
        

        self.sec_nombre = Label(self.window_2, text="Nombre")  # Definimos un título
        # Por medio de grid realizamos una ubicación en grilla y (padx y pady) le damos un padding
        self.sec_nombre.grid(row=0, column=0, padx=5, pady=5)
        # Generamos una entrada por medio de Entry
        self.sec_nombre_entry = Entry(self.window_2, textvariable=self.sec_var_nombre)
        # Ubicamos el entry al lado de su label correspondiente
        self.sec_nombre_entry.grid(row=0, column=1)

        # Repetimos la acción
        self.sec_direccion = Label(self.window_2, text="Direccion")
        self.sec_direccion.grid(row=1, column=0, padx=5, pady=5)
        self.sec_direccion_entry = Entry(self.window_2, textvariable=self.sec_var_direccion)
        self.sec_direccion_entry.grid(row=1, column=1)

        #
        self.sec_celular = Label(self.window_2, text="Celular")
        self.sec_celular.grid(row=2, column=0, padx=5, pady=5)
        self.sec_celular_entry = Entry(self.window_2, textvariable=self.sec_var_celular)
        self.sec_celular_entry.grid(row=2, column=1)


        # BOTONES

        self.sec_guardar = Button(self.window_2, 
                                  text='Guardar', 
                                  width=10, 
                                  command=lambda: self.funcion.editar_datos((self.sec_var_nombre.get(),
                                                                                    self.sec_var_direccion.get(),
                                                                                    self.sec_var_celular.get(),
                                                                                    datos[0]), 
                                                                                    self.window_2
                                                                        )
                                                    
                                )
        
        self.sec_guardar.grid(row=3, column=0, padx=20)

        self.sec_editar = Button(self.window_2, text='Cancelar', width=10, command=lambda: self.window_2.destroy())
        self.sec_editar.grid(row=3, column=1, padx=20)

        self.window_2.mainloop()