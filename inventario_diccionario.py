'''
Diccionario para el inventario
Detalle de la posible estructura del diccionario:
    - nombre: Es el nombre del producto. Es una cadena de caracteres que lo describe de manera general.
    - descripcion: Descripción más detallada del producto. Es también un texto.
    - cantidad: Cantidad disponible del producto en el inventario. Es un número entero.
    - precio: Representa el precio del producto. Es un número decimal (tipo float).
    - categoria: Indica la categoría a la que pertenece el producto. Esto nos permite organizar los productos en grupos según su tipo.
'''

inventario = {
    1: {
        "nombre" : "Manzana",
        "descripcion" : "Fruta fresca",
        "cantidad" : 50,
        "precio" : 0.5,
        "categoria" : "Frutas"
    },
    2: {
        "nombre" : "Pan",
        "descripcion" : "Pan Casero",
        "cantidad" : 20,
        "precio" : 1.0,
        "categoria" : "Panadería"
    }
}