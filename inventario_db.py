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

    cursor.execute("SELECT COUNT(*) FROM productos")
    cantidad_productos = cursor.fetchone()[0]

    if cantidad_productos == 0:
        productos_iniciales = [
            ("Manzana", "Fruta", 50, 10.20, "Frutas"),
            ("Pan", "Pan Casero", 20, 50.0, "Panadería")
        ]

        # Insertar los productos en la tabla
        # executemany --insertar varios registros al mismo tiempo
        cursor.executemany('''
            INSERT INTO productos (nombre, descripcion, stock, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', productos_iniciales)
    
    conexion.commit()
    conexion.close()

#Conexión a la base de datos.
def conexion_db():
    return sqlite3.connect('inventario.db')