#!/usr/bin/env python3
"""
Test script to verify database connection and table structure
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from repository.Conexion import conexion

def test_database_connection():
    """Test database connection and table structure"""
    try:
        # Test connection
        db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        db.connect()
        
        # Test friend table structure
        print("Testing friend table structure...")
        query = "DESCRIBE friend"
        result = db.execute_query(query)
        if result:
            print("Friend table columns:")
            for row in result:
                print(f"  {row[0]} - {row[1]}")
        
        # Test if we can select from friend table
        print("\nTesting friend table data...")
        query = "SELECT * FROM friend LIMIT 3"
        result = db.execute_query(query)
        if result:
            print("Sample friend data:")
            for row in result:
                print(f"  {row}")
        else:
            print("No friend data found (this is normal for a new database)")
        
        # Test other tables
        tables = ['category', 'object', 'loan']
        for table in tables:
            print(f"\nTesting {table} table...")
            query = f"SELECT COUNT(*) FROM {table}"
            result = db.execute_query(query)
            if result:
                print(f"  {table} table has {result[0][0]} records")
        
        db.disconnect()
        print("\nDatabase connection test successful!")
        return True
        
    except Exception as e:
        print(f"Database connection test failed: {e}")
        return False

if __name__ == "__main__":
    test_database_connection()