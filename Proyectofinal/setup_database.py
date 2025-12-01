#!/usr/bin/env python3
"""
Standalone database setup script
Run this script if you only want to setup the database without running the app
"""

from init_database import initialize_database

if __name__ == "__main__":
    print("Configurando base de datos para Book App Python...")
    if initialize_database():
        print("¡Configuración completada exitosamente!")
    else:
        print("Error en la configuración. Verifique que XAMPP esté ejecutándose.")