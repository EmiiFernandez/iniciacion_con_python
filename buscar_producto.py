import estilos
from inventario_db import conexion_db

'''
Búsqueda de productos

Frecuentemente necesitamos conocer datos de un único producto. Si bien la función mostrar_productos() que escribiste antes hace esto, lo cierto es que si tenemos muchos productos el listado puede ser demasiado extenso.

Podés crear una función más especializada (a la que llamamos buscar_producto() ) que le pida a la persona que opera el programa ingresar el código del producto que está buscando, y si el producto existe en el inventario, mostrar la información de ese único producto, con un formato claro.

TIP: Si el código que se ingresa no está registrado, podemos avisar que no se encontró el producto.
'''

def buscar_producto_por_nombre():
    print(estilos.estilo_titulo + "\n[BUSCAR PRODUCTO POR NOMBRE]")
    nombre = input("Ingrese el nombre del producto a buscar: ").capitalize()
    
    try:
        conexion = conexion_db()
        cursor = conexion.cursor()

        # Ejecutar la consulta SQL para obtener el producto por nombre
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        resultados = cursor.fetchone()

        # Comprobar si hay resultados y mostrar el producto encontrado
        if resultados:
            id, nombre, descripcion, stock, precio, categoria = resultados
            print(estilos.estilo_exito + f"\nProducto encontrado: {nombre}")
            print(f"{'ID':<5} {'Nombre':<20} {'Descripción':<30} {'Stock':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 90)
            print(f"{id:<5} {nombre:<20} {descripcion:<30} {stock:<10} {precio:<10.2f} {categoria:<15}")
        else:
            print(estilos.estilo_aviso + "Producto no encontrado.")
    except Exception as e:
        print(estilos.estilo_alerta + f"Error al buscar el producto: {e}")
    finally:
        conexion.close()