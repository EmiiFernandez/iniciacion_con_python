import estilos
from inventario_db import conexion_db

'''
Reporte de stock bajo

En muchos proyectos nos interesa conocer qué productos de nuestro inventario poseen pocas unidades. Esta información nos facilita organizar las compras y reposición de stock.
Para eso, podemos crear reporte_bajo_stock(), una función que se encargue de indicar que se ingrese un límite de stock, y luego busque en el diccionario todos los productos cuya cantidad sea igual o inferior a ese límite.
Finalmente, debería mostrar todos esos productos en pantalla.

TIP: Validá la entrada del usuario o usuaria, para evitar que se ingresen valores negativos o que no sean coherentes con la lógica de tu programa.
'''
def reporte_bajo_stock():
    print(estilos.estilo_titulo + "\n[REPORTE BAJO STOCK]")
    valor_bajo = 0

    while valor_bajo <= 0:
        try:
            valor_bajo = int(input(estilos.estilo_menu + "\nIngrese la cantidad minima de stock: "))
            if valor_bajo <=0:
                print(estilos.estilo_aviso + "\nIngrese un numero mayor que 0")
        except ValueError:
            print(estilos.estilo_aviso + "\nIngrese un numero")
            valor_bajo = 0
            
    try:
        conexion = conexion_db()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos WHERE stock <= ?", (valor_bajo,))
        resultados = cursor.fetchall()

        # Comprobar si hay resultados y mostrar productos
        if resultados:
            print(estilos.estilo_exito + f"\nProductos con stock menor o igual a {valor_bajo}:")
            print(f"{'ID':<5} {'Nombre':<20} {'Descripción':<30} {'Stock':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 90)
            
            for registro in resultados:
                id_producto, nombre, descripcion, stock, precio, categoria = registro
                print(f"{id_producto:<5} {nombre:<20} {descripcion:<30} {stock:<10} {precio:<10.2f} {categoria:<15}")
        else:
            print(estilos.estilo_exito + "No hay productos con bajo stock.")
    except Exception as e:
        print(estilos.estilo_alerta + f"Error al obtener los productos: {e}")
    finally:
        conexion.close()