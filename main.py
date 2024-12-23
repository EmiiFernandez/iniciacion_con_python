from registrar_producto import registrar_producto
from mostrar_productos import mostrar_producto

def main():
    try:
        registrar_producto()
        mostrar_producto()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()