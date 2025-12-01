#!/usr/bin/env python3
"""
Database initialization script for Book App Python
This script will automatically create the database and tables if they don't exist
"""

import mysql.connector
import sys

def create_database_connection():
    """Create connection to MySQL server (without specifying database)"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password=""
        )
        print("✓ Conectado al servidor MySQL exitosamente")
        return connection
    except mysql.connector.Error as error:
        print(f"✗ Error conectando al servidor MySQL: {error}")
        print("  Asegúrese de que XAMPP esté ejecutándose y MySQL esté activo")
        return None

def create_database_if_not_exists(connection):
    """Create the book_app database if it doesn't exist"""
    try:
        cursor = connection.cursor()
        
        # Check if database exists
        cursor.execute("SHOW DATABASES LIKE 'book_app'")
        result = cursor.fetchone()
        
        if result:
            print("✓ La base de datos 'book_app' ya existe")
        else:
            # Create database
            cursor.execute("CREATE DATABASE book_app")
            print("✓ Base de datos 'book_app' creada exitosamente")
        
        # Use the database
        cursor.execute("USE book_app")
        cursor.close()
        return True
        
    except mysql.connector.Error as error:
        print(f"✗ Error creando la base de datos: {error}")
        return False

def create_tables_if_not_exist(connection):
    """Create all necessary tables if they don't exist"""
    try:
        cursor = connection.cursor()
        
        # Create category table
        category_table = """
        CREATE TABLE IF NOT EXISTS category (
            id_category INT AUTO_INCREMENT PRIMARY KEY,
            description VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(category_table)
        print("✓ Tabla 'category' verificada/creada")
        
        # Create friend table with correct column names
        friend_table = """
        CREATE TABLE IF NOT EXISTS friend (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(20),
            mail VARCHAR(255),
            adress VARCHAR(255),
            rol INT
        )
        """
        cursor.execute(friend_table)
        print("✓ Tabla 'friend' verificada/creada")
        
        # Create object table
        object_table = """
        CREATE TABLE IF NOT EXISTS object (
            id_object INT AUTO_INCREMENT PRIMARY KEY,
            description VARCHAR(255) NOT NULL,
            state ENUM('available', 'loaned') DEFAULT 'available',
            category_id INT,
            FOREIGN KEY (category_id) REFERENCES category(id_category) ON DELETE SET NULL
        )
        """
        cursor.execute(object_table)
        print("✓ Tabla 'object' verificada/creada")
        
        # Create loan table
        loan_table = """
        CREATE TABLE IF NOT EXISTS loan (
            id_loan INT AUTO_INCREMENT PRIMARY KEY,
            date_loan DATE NOT NULL,
            date_return DATE,
            friend_id INT,
            object_id INT,
            state ENUM('active', 'returned', 'overdue') DEFAULT 'active',
            FOREIGN KEY (friend_id) REFERENCES friend(id) ON DELETE CASCADE,
            FOREIGN KEY (object_id) REFERENCES object(id_object) ON DELETE CASCADE
        )
        """
        cursor.execute(loan_table)
        print("✓ Tabla 'loan' verificada/creada")
        
        connection.commit()
        cursor.close()
        return True
        
    except mysql.connector.Error as error:
        print(f"✗ Error creando las tablas: {error}")
        return False

def insert_sample_data_if_empty(connection):
    """Insert sample data if tables are empty"""
    try:
        cursor = connection.cursor()
        
        # Check if category table has data
        cursor.execute("SELECT COUNT(*) FROM category")
        category_count = cursor.fetchone()[0]
        
        if category_count == 0:
            print("→ Insertando datos de ejemplo en categorías...")
            categories = [
                ('Libros',),
                ('Herramientas',),
                ('Electrodomésticos',),
                ('Deportes',),
                ('Música',)
            ]
            cursor.executemany("INSERT INTO category (description) VALUES (%s)", categories)
            print("✓ Categorías de ejemplo insertadas")
        else:
            print(f"✓ La tabla category ya tiene {category_count} registros")
        
        # Check if friend table has data
        cursor.execute("SELECT COUNT(*) FROM friend")
        friend_count = cursor.fetchone()[0]
        
        if friend_count == 0:
            print("→ Insertando datos de ejemplo de amigos...")
            friends = [
                ('Juan Pérez', '3001234567', 'juan@email.com', 'Calle 123', 1),
                ('María García', '3009876543', 'maria@email.com', 'Carrera 456', 1),
                ('Carlos López', '3005555555', 'carlos@email.com', 'Avenida 789', 1)
            ]
            cursor.executemany("INSERT INTO friend (name, phone, mail, adress, rol) VALUES (%s, %s, %s, %s, %s)", friends)
            print("✓ Amigos de ejemplo insertados")
        else:
            print(f"✓ La tabla friend ya tiene {friend_count} registros")
        
        # Check if object table has data
        cursor.execute("SELECT COUNT(*) FROM object")
        object_count = cursor.fetchone()[0]
        
        if object_count == 0:
            print("→ Insertando datos de ejemplo de objetos...")
            objects = [
                ('El Quijote', 'available', 1),
                ('Taladro Eléctrico', 'available', 2),
                ('Licuadora', 'available', 3),
                ('Balón de Fútbol', 'available', 4),
                ('Guitarra Acústica', 'available', 5),
                ('Cien Años de Soledad', 'loaned', 1),
                ('Martillo', 'available', 2)
            ]
            cursor.executemany("INSERT INTO object (description, state, category_id) VALUES (%s, %s, %s)", objects)
            print("✓ Objetos de ejemplo insertados")
        else:
            print(f"✓ La tabla object ya tiene {object_count} registros")
        
        connection.commit()
        cursor.close()
        return True
        
    except mysql.connector.Error as error:
        print(f"✗ Error insertando datos de ejemplo: {error}")
        return False

def fix_existing_table_structure(connection):
    """Fix table structure if it doesn't match our application"""
    try:
        cursor = connection.cursor()
        
        # Check if friend table exists
        cursor.execute("SHOW TABLES LIKE 'friend'")
        result = cursor.fetchone()
        
        if not result:
            print("→ La tabla friend no existe, será creada en el siguiente paso")
            cursor.close()
            return True
        
        # Check current friend table structure
        cursor.execute("DESCRIBE friend")
        columns = cursor.fetchall()
        column_names = [col[0] for col in columns]
        
        print(f"→ Estructura actual de la tabla friend: {column_names}")
        
        # If the table has the wrong structure, recreate it
        if 'id_friend' in column_names or 'email' in column_names:
            print("→ La tabla friend tiene estructura incorrecta, recreando...")
            
            # Backup existing data if any
            cursor.execute("SELECT COUNT(*) FROM friend")
            if cursor.fetchone()[0] > 0:
                print("→ Respaldando datos existentes...")
                cursor.execute("CREATE TEMPORARY TABLE friend_backup AS SELECT * FROM friend")
            
            # Drop and recreate table
            cursor.execute("DROP TABLE IF EXISTS friend")
            friend_table = """
            CREATE TABLE friend (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                phone VARCHAR(20),
                mail VARCHAR(255),
                adress VARCHAR(255),
                rol INT
            )
            """
            cursor.execute(friend_table)
            print("✓ Tabla friend recreada con estructura correcta")
        else:
            print("✓ La tabla friend ya tiene la estructura correcta")
        
        connection.commit()
        cursor.close()
        return True
        
    except mysql.connector.Error as error:
        print(f"✗ Error arreglando estructura de tabla: {error}")
        cursor.close()
        return False

def initialize_database():
    """Main function to initialize the database"""
    print("=" * 60)
    print("    INICIALIZADOR DE BASE DE DATOS - BOOK APP PYTHON")
    print("=" * 60)
    
    # Step 1: Connect to MySQL server
    connection = create_database_connection()
    if not connection:
        return False
    
    # Step 2: Create database if not exists
    if not create_database_if_not_exists(connection):
        connection.close()
        return False
    
    # Step 3: Fix table structure if needed
    if not fix_existing_table_structure(connection):
        connection.close()
        return False
    
    # Step 4: Create tables if not exist
    if not create_tables_if_not_exist(connection):
        connection.close()
        return False
    
    # Step 5: Insert sample data if empty
    if not insert_sample_data_if_empty(connection):
        connection.close()
        return False
    
    # Close connection
    connection.close()
    
    print("=" * 60)
    print("    ✓ BASE DE DATOS INICIALIZADA EXITOSAMENTE")
    print("=" * 60)
    print("La aplicación está lista para usar.")
    print("Ejecute: python3 main.py")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    try:
        initialize_database()
    except KeyboardInterrupt:
        print("\n\nInicialización cancelada por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        print("Verifique que XAMPP esté ejecutándose correctamente.")