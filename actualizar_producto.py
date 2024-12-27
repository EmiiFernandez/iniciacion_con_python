import estilos
from inventario_db import conexion_db
from mostrar_productos import mostrar_productos

'''
Actualización de productos

En aplicaciones como la que estamos desarrollando, es necesario contar con una opción que permita actualizar los datos almacenados. Para ello, escribiremos la función actualizar_producto().

Esta función debería solicitar que se ingrese el código del producto a actualizar, y verificar si existe en nuestro diccionario. En caso afirmativo se piden el o los datos a actualizar y se efectúa el reemplazo de los valores en el diccionario. Si el producto cuyo código hemos ingresado no existe, se puede mostrar un mensaje explicando la situación antes de salir de la función.

Por supuesto, ¡puedes agregar todas las funcionalidades extra que consideres necesario!
'''

def actualizar_producto():
    print(estilos.estilo_titulo + "\n[ACTUALIZAR PRODUCTO]")

    print(estilos.estilo_aviso + "\nLos productos en el inventario son: ")
    mostrar_productos()

    id = 0

    while id <= 0:
        try:
            id = int(input("Ingrese el código del producto a modificar/actualizar: "))

            # Verificar si el producto existe en la base de datos
            conexion = conexion_db()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
            producto = cursor.fetchone()

            if not producto:
                print(estilos.estilo_alerta + f"El código {id} no existe en la base de datos.")
                conexion.close()
                id = 0
                continue

            print(estilos.estilo_exito + "\nProducto encontrado:")
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Stock: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")

            print(estilos.estilo_aviso + "\nPresione ENTER para mantener el valor actual")

            # Pedir datos al usuario, dejando la posibilidad de mantener los valores actuales
            nombre = input(f"Nombre actual ({producto[1]}): ").capitalize() or producto[1]
            descripcion = input(f"Descripción actual ({producto[2]}): ").capitalize() or producto[2]
            categoria = input(f"Categoría actual ({producto[5]}): ").capitalize() or producto[5]

            # Validar cantidad
            stock = producto[3]
            while True:
                try:
                    stock_input = input(f"Stock actual ({producto[3]}): ")
                    if stock_input == "":
                        break
                    stock = int(stock_input)
                    if stock <= 0:
                        print(estilos.estilo_alerta + "Ingrese un número mayor que 0.")
                        continue
                    break
                except ValueError:
                    print(estilos.estilo_alerta + "Ingrese un número válido.")

            # Validar precio
            precio = producto[4]
            while True:
                try:
                    precio_input = input(f"Precio actual ({producto[4]}): ")
                    if precio_input == "":
                        break
                    precio = float(precio_input)
                    if precio <= 0:
                        print(estilos.estilo_alerta + "Ingrese un número mayor que 0.")
                        continue
                    break
                except ValueError:
                    print(estilos.estilo_alerta + "Ingrese un número válido.")

            # Actualizar en la base de datos
            cursor.execute(
                '''UPDATE productos SET nombre = ?, descripcion = ?, stock = ?, precio = ?, categoria = ? WHERE id = ?''',
                (nombre, descripcion, stock, precio, categoria, id)
            )
            conexion.commit()
            conexion.close()

            print(estilos.estilo_exito + f"\nProducto actualizado con éxito:\n")
            
            print(estilos.estilo_titulo + f"{'ID':<5} {'Nombre':<20} {'Descripción':<30} {'Stock':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 90)
            print(f"{id:<5} {nombre:<20} {descripcion:<30} {stock:<10} {precio:<10.2f} {categoria:<15}")

        except ValueError:
            print(estilos.estilo_alerta + "Ingrese un código válido.")
            id = 0
