from database import SQLite as sql
from tkinter import messagebox

##### PARA PROBAR LA APP EJECUTAR DESDE VIEW.PY ##################

class Funciones:
    def __init__(self, tabla):
        self.tabla = tabla
        self.conectar = sql()
        self.__reiniciar_tabla()
        self.__recuperar_datos()

    def guardar_datos(self, tupla_de_datos: tuple):
        self.conectar.insert(tupla_de_datos)
        self.__reiniciar_tabla()
        self.__recuperar_datos()
        
    def editar_datos(self, tupla_de_datos: tuple, window):
        self.conectar.update(tupla_de_datos)
        window.destroy()
        self.__reiniciar_tabla()
        self.__recuperar_datos()
    

    def eliminar_datos(self, cadena:str):
        lista = self.dato_seleccionado()
        if self.comprobar_contacto(lista, cadena):
            self.conectar.delete(lista[0])

        self.__reiniciar_tabla()
        self.__recuperar_datos()


    def dato_seleccionado(self):
        lista = []
        
        current_item = self.tabla.focus()
        if not current_item:
            return []
        data = self.tabla.item(current_item)

        lista.append(data['text'])
        lista.extend(data['values'])
        
        return lista

    def comprobar_contacto(self, lista, cadena):
        cadena = ("Contacto no seleccionado", "Por favor seleccione un contacto para " + cadena)
        if len(lista) == 0:
            messagebox.showwarning(cadena[0], cadena[1])
            return False
        return True
        
    def rellenar_campos(self, tupla, lista):
        tupla[0].set(lista[1])
        tupla[1].set(lista[2])
        tupla[2].set(lista[3])
    

    def __reiniciar_tabla(self):
        borrar = self.tabla.get_children()
        
        for elemento in borrar:
            self.tabla.delete(elemento)
    
    def __recuperar_datos(self):
        lista_de_datos = self.conectar.select_all()
        print(lista_de_datos)
        for i in lista_de_datos:
            self.tabla.insert('', 'end', text=i[0], values=(i[1], i[2], i[3]))

        
