import sqlite3


class SQLite:
    
    def __init__(self):
    
        self.__crear_tabla()
        

    def __crear_tabla(self):
        self.mi_base = sqlite3.connect("agenda.db")

        self.cursor = self.mi_base.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS contactos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(40) NOT NULL,
                    direccion VARCHAR(100) NOT NULL,
                    celular INTEGER NOT NULL
                    );""")
        self.mi_base.commit()
        self.mi_base.close()

    def select_all(self):
        print("select all")
        self.mi_base = sqlite3.connect("agenda.db")

        self.cursor = self.mi_base.cursor()
        """Completar con lógica para obtener todos los datos de la tabla de la base de datos."""
        
        consulta = "SELECT * FROM contactos;"
        self.cursor.execute(consulta)
        datos = self.cursor.fetchall()
        self.mi_base.close()
        # datos = None  # Cambiar el valor None por una lista obtenida de la consulta
        return datos

    def insert(self, datos: tuple):
        self.mi_base = sqlite3.connect("agenda.db")

        self.cursor = self.mi_base.cursor()
        """Completar con lógica para insertar los datos en la tabla"""

        
        consulta = "INSERT INTO contactos (nombre, direccion, celular) VALUES (?, ?, ?);"
        self.cursor.execute(consulta, datos)

        self.mi_base.commit()
        self.mi_base.close()

    def update(self, datos):
        parametros = tuple(datos)
        mi_base = sqlite3.connect("agenda.db")
        cursor = mi_base.cursor()
        consulta = "UPDATE contactos SET nombre = ?, direccion = ?, celular = ? WHERE id = ?;"
        cursor.execute(consulta, parametros)
        mi_base.commit()
        mi_base.close()
    
    def delete(self, datos):
        parametros = (datos,)
        mi_base = sqlite3.connect("agenda.db")
        cursor = mi_base.cursor()
        consulta = "DELETE FROM contactos WHERE id=?;"
        cursor.execute(consulta, parametros)
        mi_base.commit()
        mi_base.close()

    
