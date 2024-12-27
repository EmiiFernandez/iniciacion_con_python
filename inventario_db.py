import sqlite3

#Crea la base de datos y la tabla si no existen.
def inicializar_db():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            stock INTEGER NOT NULL CHECK(stock >= 0),
            precio REAL NOT NULL CHECK(precio >= 0),
            categoria TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

#Conexión a la base de datos.
def conexion_db():
    return sqlite3.connect('inventario.db')