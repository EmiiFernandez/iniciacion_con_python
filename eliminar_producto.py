import estilos
from inventario_db import conexion_db
from mostrar_productos import mostrar_productos

'''
Eliminación de productos

En algún momento vas a necesitar quitar elementos de tu lista de productos. Productos obsoletos, o que no desees comercializar más, deberían ser quitados del diccionario para que no ocupen lugar o demoren innecesariamente las búsquedas.

eliminar_producto() debe pedir el código del producto a borrar, buscarlo en el diccionario, y si lo encuentra, quitarlo de él. Si no lo encuentra,podemos notificar a la usuaria o usuario de esta situación.

TIP: Es posible que puedas utilizar en esta función un algoritmo similar el que usaste en actualizar_producto()
'''

def eliminar_producto():
    print(estilos.estilo_titulo + "\n[ELIMINAR PRODUCTO]")

    # Verificar si hay productos en el inventario
    conexion = conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if not productos:
        print(estilos.estilo_alerta + "No hay productos en el inventario.")
        conexion.close()
        return

    print(estilos.estilo_aviso + "\nLos productos en el inventario son:")
    mostrar_productos()

    id = 0

    while id <= 0:
        try:
            id = int(input("Ingrese el código del producto a eliminar: "))

            # Verificar si el producto existe en la base de datos
            cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
            producto = cursor.fetchone()

            if not producto:
                print(estilos.estilo_alerta + f"El código {id} no existe en la base de datos.")
                id = 0
                continue

            print(estilos.estilo_exito + "\nProducto encontrado:")
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Stock: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")

            confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").strip().lower()
            if confirmacion == 's':
                # Eliminar el producto de la base de datos
                cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
                conexion.commit()
                print(estilos.estilo_exito + f"\nEl producto con ID {id} ha sido eliminado con éxito.")
            else:
                print(estilos.estilo_aviso + "Operación cancelada.")

            break

        except ValueError:
            print(estilos.estilo_alerta + "Ingrese un código válido.")
            id = 0

    conexion.close()
