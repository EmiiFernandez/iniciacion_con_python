'''
Listado de productos

Nuestro proyecto necesita una función que se encargue de mostrar una lista todos los productos que están almacenados en el diccionario inventario.La hemos llamado mostrar_productos().

El código de esta función debe recorrer todo el inventario y mostrar la información de cada producto de manera clara, incluyendo su código, nombre descripción, cantidad, precio y categoría. Para ello puedes usar un bucle.

Ten en cuenta que si el inventario está vacío, la función debería informar que aún no han ingresado productos
'''

from inventario_diccionario import inventario

def mostrar_productos():
    if len(inventario) == 0:
        print("El inventario está vacío")
    else:
        print(f"{'codigo':<10}{'nombre':<20}{'descripcion':<20}{'cantidad':<5}{'precio':<5}{'categoria':<10}")

        for codigo, producto in inventario.items():
            print(f"{codigo:<10}{producto['nombre']:<20}{producto['descripcion']:<20}{producto['cantidad']:<5}{producto['precio']:<5}{producto['categoria']:<10}")

