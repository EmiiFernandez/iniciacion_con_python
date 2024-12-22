"""
1. Crear un menú interactivo
Crear un menú interactivo utilizando bucles while y condicionales if-elif-else:
● El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos.
● Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados.
2. Agregar productos al inventario
Implementar la funcionalidad para agregar productos a una lista:
● Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada.
3. Mostrar el inventario
Mostrar los productos ingresados:
● Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el
momento.
"""
productos = []

# Productos para realiza pruebas
productos_mockeados = [
    [123, "Manzana", 10, 1.50],
    [456, "Banana", 2, 0.80],
    [789, "Naranja", 2, 1.20]
]

while True:
    # Menú principal
    print("\nMenú de Gestión de Productos\n")
    print("1. Alta de productos nuevos")
    print("2. Consulta de datos de productos")
    print("3. Modificar la cantidad en stock de un producto")
    print("4. Dar de baja productos")
    print("5. Listado completo de los productos")
    print("6. Lista de productos con cantidad bajo mínimo")
    print("7. Salir\n")
    
    # Ingresar por teclado una opción
    opcion = int(input("Seleccioná una opción: "))

    # Métodos según la opción elegida
    if opcion == 1:
        print("\n1. Alta de productos nuevos\n")

        while True:
            codigo = int(input("Ingresá el código del producto (0 para finalizar): "))

            if codigo == 0:
                break
        
            nombre = input("Ingresá el nombre del producto: ").capitalize()
            cantidad = int(input("Ingresá la cantidad del producto: "))    
            precio = float(input("Ingresá el precio del producto: "))

            productos.append([codigo, nombre, cantidad, precio])
    
    if opcion == 2:
        print("\n2. Consulta de datos de productos\n")

        while True: 
            nombre = input("Ingresá el nombre del producto (0 para volver al menú principal): ").capitalize()

            if nombre == "0":
                break

            for producto in productos:
                if nombre ==  producto[1]:
                    print("Código:", producto[0], "- Nombre:", producto[1], "- Cantidad:", producto[2], "- Precio: $", producto[3])
                    break

            if nombre != producto[1]:
                print("Producto no encontrado")
                    
    
    if opcion == 5:
        print("\n5. Listado completo de los productos")

        for producto in productos:
            print("Código:", producto[0], "- Nombre:", producto[1], "- Cantidad:", producto[2], "- Precio: $", producto[3])

    if opcion == 6:
        print("\n6. Lista de productos con cantidad bajo mínimo\n")

        for producto in productos:
            if producto[2] < 3:
                print("Código:", producto[0], "- Nombre:", producto[1], "- Cantidad:", producto[2], "- Precio: $", producto[3])

    if opcion == 7:
        print("Salir del programa")
        break

    
''''try:
        ....
except ValueError:
    print ("Error: ", ValueError)
    print ("Debe ingresar un número")'''