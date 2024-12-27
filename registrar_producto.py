import estilos
from inventario_db import conexion_db

'''
Registro de productos

Necesitamos una función registrar_producto() que se encargue de agregar los productos en el diccionario inventario con un código único y sus respectivos datos. La función pedirá que se ingrese los detalles del producto y los almacenará en el diccionario.
Usaremos una variable que actúe como un contador para los códigos de los productos, así cada vez que se registra un producto, se le asigna automáticamente un código nuevo.

El diccionario inventario usará el código del producto como clave, mientras que los valores asociados a esa clave serán otro diccionario que contendrá toda la información del producto.
'''

#Verifica si un producto con el mismo nombre ya existe en la base de datos.
def verificar_producto_existente(nombre):
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos WHERE nombre = ?", (nombre,))
    existe = cursor.fetchone()[0] > 0
    conexion.close()
    return existe

# Valida que la cantidad de stock sea mayor que 0.
def validar_stock(cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad en stock debe ser un número positivo mayor a 0.")

# Valida que el precio sea mayor que 0.
def validar_precio(precio):
    if precio <= 0:
        raise ValueError("El precio debe ser un número positivo mayor a 0.")
    
# Registra un producto en la base de datos si no existe y valida los datos ingresados.
def registrar_producto():
    print(estilos.estilo_titulo + "\n[REGISTRO DE PRODUCTO]")

    nombre = input("Ingrese el nombre del producto: ").capitalize()
    descripcion = input("Ingrese la descripción del producto: ").capitalize()
    categoria = input("Ingrese la categoría del producto: ").capitalize()
  # Validación de stock y precio
    while True:
        try:
            stock = int(input("Ingrese la cantidad en stock: "))
            validar_stock(stock)
            break  # Si pasa la validación, salimos del bucle
        except ValueError as e:
            print(estilos.estilo_alerta + str(e))

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            validar_precio(precio)
            break  # Si pasa la validación, salimos del bucle
        except ValueError as e:
            print(estilos.estilo_alerta + str(e))

    # Verificar si el producto ya existe
    if verificar_producto_existente(nombre):
        print(estilos.estilo_alerta + f"El producto '{nombre}' ya existe en la base de datos.")
        return

    datos = [nombre, descripcion, stock, precio, categoria]
    conexion = conexion_db()
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO productos (nombre, descripcion, stock, precio, categoria) VALUES (?, ?, ?, ?, ?)", datos)
    conexion.commit()
    print(estilos.estilo_exito + f"Producto '{nombre}' agregado con éxito.")
    conexion.close()