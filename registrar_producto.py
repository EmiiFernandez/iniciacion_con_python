'''
Registro de productos

Necesitamos una función registrar_producto() que se encargue de agregar los productos en el diccionario inventario con un código único y sus respectivos datos. La función pedirá que se ingrese los detalles del producto y los almacenará en el diccionario.
Usaremos una variable que actúe como un contador para los códigos de los productos, así cada vez que se registra un producto, se le asigna automáticamente un código nuevo.

El diccionario inventario usará el código del producto como clave, mientras que los valores asociados a esa clave serán otro diccionario que contendrá toda la información del producto.
'''

from inventario_diccionario import inventario

def registrar_producto():
    codigo_producto = len(inventario) + 1
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    descripcion = input("Ingrese la descripción del producto: ").capitalize()
    categoria = input("Ingrese la categoría del producto: ").capitalize()
    cantidad = 0
    precio = 0

    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad del stock: "))
            if cantidad <= 0:
                print ("Ingrese un número mayor que 0")
        except:
            print("Ingrese un número mayor a 0")
            cantidad = 0

        while precio <= 0:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print ("Ingrese un número mayor que 0")
            except:
                print("Ingrese un número mayor a 0")
                precio = 0
    
    '''Agregar al inventario'''

    inventario[codigo_producto] = {
        "nombre" : nombre,
        "descripcion" : descripcion,
        "cantidad" : cantidad,
        "precio" : precio,
        "categoria" : categoria
    }

    print("Producto agregado correctamente:\n", inventario[codigo_producto])
    
registrar_producto()

'''
Separar en funcione el precio y la cantidad

Verificar si el producto existe
'''