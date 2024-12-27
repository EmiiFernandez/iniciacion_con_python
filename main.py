from inventario_db import inicializar_db
from menu_principal import menu_principal



def main():
        
        inicializar_db()
        menu_principal()

if __name__ == "__main__":
    main()