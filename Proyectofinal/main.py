#!/usr/bin/env python3
"""
Main entry point for the Book App Python application.
This script initializes and runs the application.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from view.App import App
from init_database import initialize_database

def main():
    """Initialize and run the application."""
    try:
        print("Verificando base de datos...")
        
        # Try to initialize database first
        if not initialize_database():
            print("Error inicializando la base de datos. Verifique que XAMPP esté ejecutándose.")
            return
        
        print("\n¡Base de datos lista! Iniciando aplicación...\n")
        
        app = App()
        app.run_app()
    except KeyboardInterrupt:
        print("\n\nAplicación interrumpida por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        print("Por favor, verifique la conexión a la base de datos y que XAMPP esté ejecutándose.")

if __name__ == "__main__":
    main()

    #Objeto
    #Revisar porqué duplicidad de prestamos


