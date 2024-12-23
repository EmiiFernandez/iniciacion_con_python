'''
Actualización de productos

En aplicaciones como la que estamos desarrollando, es necesario contar con una opción que permita actualizar los datos almacenados. Para ello, escribiremos la función actualizar_producto().

Esta función debería solicitar que se ingrese el código del producto a actualizar, y verificar si existe en nuestro diccionario. En caso afirmativo se piden el o los datos a actualizar y se efectúa el reemplazo de los valores en el diccionario. Si el producto cuyo código hemos ingresado no existe, se puede mostrar un mensaje explicando la situación antes de salir de la función.

Por supuesto, ¡puedes agregar todas las funcionalidades extra que consideres necesario!
'''

from inventario_diccionario import inventario
from mostrar_productos import mostrar_productos

def actualizar_producto():
    print("Los productos en el inventario son: ")
    mostrar_productos()
    codigo_producto = 0
    
    while codigo_producto <= 0:
        try:
            codigo_producto = int(input("Ingrese la código del producto a modificar/actualizar: "))

            producto = inventario.get(codigo_producto , "No encontrado")

            if producto == "No encontrado":
                print(f"El código {codigo_producto} no existe en el inventario")
                codigo_producto = 0 
            else:
                print("\nProducto encontrado:")
                print(f"{codigo_producto:<10}{producto['nombre']:<20}{producto['descripcion']:<20}{producto['cantidad']:<5}{producto['precio']:<5}{producto['categoria']:<10}")
 
                print("\nPresione ENTER para mantener el valor actual")
                
                nombre = input(f"Nombre actual: {producto['nombre']}\nNuevo nombre: ").capitalize()
                nombre = nombre if nombre != "" else producto['nombre']
                
                descripcion = input(f"Descripción actual: {producto['descripcion']}\nNueva descripción: ").capitalize()
                descripcion = descripcion if descripcion != "" else producto['descripcion']
                
                categoria = input(f"Categoría actual: {producto['categoria']}\nNueva categoría: ").capitalize()
                categoria = categoria if categoria != "" else producto['categoria']
                
                cantidad = producto['cantidad']   
                while True:
                    try:
                        cant_input = input(f"Cantidad actual: {producto['cantidad']}\nNueva cantidad (ENTER para mantener): ")
                        if cant_input == "":  
                            break
                        cantidad = int(cant_input)
                        if cantidad <= 0:
                            print("Ingrese un número mayor que 0")
                            continue
                        break
                    except ValueError:
                        print("Ingrese un número válido")

                precio = producto['precio'] 
                while True:
                    try:
                        precio_input = input(f"Precio actual: {producto['precio']}\nNuevo precio (ENTER para mantener): ")
                        if precio_input == "":   
                            break
                        precio = float(precio_input)
                        if precio <= 0:
                            print("Ingrese un número mayor que 0")
                            continue
                        break
                    except ValueError:
                        print("Ingrese un número válido")

                inventario[codigo_producto] = {
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "cantidad": cantidad,
                    "precio": precio,
                    "categoria": categoria
                }


                print("Producto agregado exitosamente:\n", inventario[codigo_producto])
    
        except ValueError:
                print("Ingrese un número")
                codigo_producto = 0

actualizar_producto()   
