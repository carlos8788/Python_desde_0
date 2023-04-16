import sqlite3
##### PARA PROBAR LA APP EJECUTAR DESDE VIEW.PY ##################

class SQLite:
    
    def __init__(self):
    
        self.__crear_tabla()
        

    def __crear_tabla(self):
        """Creacion de tabla con los campos:
        id entero
        nombre varchar
        direccion varchar
        celular entero
        """
        print("conectar tabla")
        

    def select_all(self):
        print("Consultar datos")
        """Completar con lógica para obtener todos los datos de la tabla de la base de datos."""
        datos = None  # Cambiar el valor None por una lista obtenida de la consulta
        return datos

    def insert(self, datos: tuple):
        """la variable datos trae (nombre, direccion, celular) """
        print("Insertar datos")
        """Completar con lógica para insertar los datos en la tabla"""


    def update(self, datos):
        """la variable datos trae (nombre, direccion, celular, id) """
        print("Actualizar datos")
        """Completar con la lógica para actualizar los datos"""
    
        
    def delete(self, datos):
        """la variable datos trae (id) """
        print("Eliminar datos")
        """Completar con la lógica para elimiar un contacto"""
       
    
