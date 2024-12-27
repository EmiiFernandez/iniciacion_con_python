import estilos
from registrar_producto import registrar_producto 
from buscar_producto import buscar_producto_por_nombre 
from actualizar_producto import actualizar_producto 
from eliminar_producto import eliminar_producto 
from mostrar_productos import mostrar_productos 
from reporte_bajo_stock import reporte_bajo_stock

'''
Menú principal

En clases anteriores hemos analizado la utilidad que tiene dotar a nuestra aplicación de un menú que permita a la persona que lo utiliza acceder a las funciones que hemos desarrollado.

Por ejemplo, nuestro menú principal podría mostrar las distintas acciones disponibles (registrar productos, mostrar el inventario, actualizar productos, eliminarlos, buscarlos y generar reportes de bajo stock). Se seleccionará la acción escribiendo el número de la opción que se desea accionar y el programa entonces ejecutaría la función correspondiente.

TIP: ¡ El menú principal también puede ser una función!
'''
def menu_principal() :
    menu = True

    while menu:

        print(estilos.estilo_menu + "\n[MENU PRINCIPAL]")
        print("\nMenú de Gestión de Productos\n")
        print("1. Alta de productos nuevos")
        print("2. Listado completo de los productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Reporte de bajo stock")
        print("6. Buscar producto por nombre")
        print("7. Salir\n")

        # Ingresar por teclado una opción
        opcion = int(input("Seleccione una opción: "))

        # Métodos según la opción elegida
        if opcion == 1:
            registrar_producto()
        elif opcion == 2:
             mostrar_productos()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            reporte_bajo_stock()
        elif opcion == 6:
            buscar_producto_por_nombre()
        elif opcion == 7:
            menu = False
            print(estilos.estilo_aviso + "Saliendo del programa...")
            break
        else:
            print(estilos.estilo_alerta + "Opción no válida.")



