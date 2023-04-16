import sqlite3

# CREAR LA BASE DE DATOS

# mi_base = sqlite3.connect("mi_base.db")

# # Creamos el cursor y luego ejecutamos el método execute() con la consulta en formato string
# cursor = mi_base.cursor()

# cursor.execute("""CREATE TABLE mi_tabla (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                nombre VARCHAR(50),
#                apellido VARCHAR(20)
#                );""")

# mi_base.close()

# mi_base = sqlite3.connect("mi_base.db")
# cursor = mi_base.cursor()
# cursor.execute("""INSERT INTO mi_tabla (nombre, apellido) VALUES ('Luis', 'Perez')""") 
# # Para guardar los datos usaremos un método llamado commit()
# mi_base.commit()
# mi_base.close()

# mi_base = sqlite3.connect("mi_base.db")
# cursor = mi_base.cursor()
# cursor.execute("""SELECT * FROM mi_tabla""") 
# datos = cursor.fetchall()

# mi_base.close()

# cursor.execute("""SELECT id, nombre, apellido FROM mi_tabla WHERE id=1""")


# mi_base = sqlite3.connect("mi_base.db")
# cursor = mi_base.cursor()
# cursor.execute("""UPDATE mi_tabla SET nombre='Carlos' WHERE id=1""") 
# mi_base.commit()
# mi_base.close()


# mi_base = sqlite3.connect("mi_base.db")
# cursor = mi_base.cursor()
# cursor.execute("""DELETE FROM mi_tabla WHERE id=1""") 
# mi_base.commit()
# mi_base.close()

# BUENAS PRÁCTICAS

# parametros = (1,) # Si tenemos un solo dato como parametro en este caso es indispensable colocar la coma al final para que entienda que es una tupla
# consulta = "SELECT id, nombre, apellido FROM mi_tabla WHERE id = ?"
# cursor.execute(consulta, parametros)
# datos = cursor.fetchall()
# print(datos)
# mi_base.close()

# parametros = ('Franco', 'Armani')
# consulta = "INSERT INTO mi_tabla (nombre, apellido) VALUES (?, ?)"
# cursor.execute(consulta, parametros)
# # Para guardar los datos usaremos un método llamado commit()
# mi_base.commit()
# mi_base.close()

# parametros = ('Constanzo', 3)
# consulta = "UPDATE mi_tabla SET apellido=? WHERE id=?"
# cursor.execute(consulta, parametros)
# # Para guardar los datos usaremos un método llamado commit()
# mi_base.commit()
# mi_base.close()

# parametros = (2,)
# consulta = "DELETE FROM mi_tabla WHERE id=?"
# cursor.execute(consulta, parametros)
# mi_base.commit()
# mi_base.close()

# CREAR LA BASE DE DATOS
def crear_tabla():
    mi_base = sqlite3.connect("electrodomesticos.db")

    # # Creamos el cursor y luego ejecutamos el método execute() con la consulta en formato string
    cursor = mi_base.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS mis_electrodomesticos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_producto VARCHAR(40) NOT NULL,
                stock INTEGER,
                precio FLOAT NOT NULL,
                descripcion VARCHAR(255) 
                );""")
    mi_base.close()

def insertar_datos(parametros):
    mi_base = sqlite3.connect("electrodomesticos.db")
    cursor = mi_base.cursor()
    
    consulta = "INSERT INTO mis_electrodomesticos (nombre_producto, stock, precio, descripcion) VALUES (?, ?, ?, ?);"
    cursor.execute(consulta, parametros)
    
    mi_base.commit()
    mi_base.close()

def consultar_datos():
    mi_base = sqlite3.connect("electrodomesticos.db")
    cursor = mi_base.cursor()
    consulta = "SELECT * FROM mis_electrodomesticos;"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    print(datos)

def consultar_dato(id):
    parametros = (id,)
    mi_base = sqlite3.connect("electrodomesticos.db")
    cursor = mi_base.cursor()
    consulta = "SELECT * FROM mis_electrodomesticos WHERE id=?;"
    cursor.execute(consulta, parametros)
    datos = cursor.fetchall()
    print(datos)

def actualizar_datos(stock, precio, descripcion, nombre_producto):
    parametros = (stock, precio, descripcion, nombre_producto)
    mi_base = sqlite3.connect("electrodomesticos.db")
    cursor = mi_base.cursor()
    consulta = "UPDATE mis_electrodomesticos SET stock = ?, precio = ?, descripcion = ? WHERE nombre_producto = ?;"
    cursor.execute(consulta, parametros)
    mi_base.commit()
    mi_base.close()

def eliminar_datos(id):
    parametros = (id,)
    mi_base = sqlite3.connect("electrodomesticos.db")
    cursor = mi_base.cursor()
    consulta = "DELETE FROM mis_electrodomesticos WHERE id=?;"
    cursor.execute(consulta, parametros)
    mi_base.commit()
    mi_base.close()

if __name__ == "__main__":
    # actualizar_datos(9, 9000, "Licuadora de 5 velocidades y jarra de vidrio", "Licuadora")
    # consultar_dato(1)
    consultar_datos()
    eliminar_datos(2)
    consultar_datos()