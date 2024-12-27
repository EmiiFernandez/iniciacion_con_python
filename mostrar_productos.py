import estilos
from inventario_db import conexion_db

'''
Listado de productos

Nuestro proyecto necesita una función que se encargue de mostrar una lista todos los productos que están almacenados en el diccionario inventario.La hemos llamado mostrar_productos().

El código de esta función debe recorrer todo el inventario y mostrar la información de cada producto de manera clara, incluyendo su código, nombre descripción, cantidad, precio y categoría. Para ello puedes usar un bucle.

Ten en cuenta que si el inventario está vacío, la función debería informar que aún no han ingresado productos
'''

from inventario_diccionario import inventario

def mostrar_productos():
    print(estilos.estilo_titulo + "\n[MOSTRAR PRODUCTOS]")

    try:
        conexion = conexion_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        
        if not resultados:
            print(estilos.estilo_aviso + "Aún no han ingresado productos.")
        else:
            print(estilos.estilo_exito + f"{'ID':<5} {'Nombre':<20} {'Descripción':<30} {'Stock':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 90)
            for registro in resultados:
                id_producto, nombre, descripcion, stock, precio, categoria = registro
                print(f"{id_producto:<5} {nombre:<20} {descripcion:<30} {stock:<10} {precio:<10.2f} {categoria:<15}")
    except Exception as e:
        print(estilos.estilo_alerta + f"Error al mostrar los productos: {e}")
    finally:
        conexion.close()