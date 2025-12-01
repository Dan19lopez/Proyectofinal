import csv
import os
from datetime import datetime
from repository.FriendRepositoryDB import FriendRepositoryDB
from repository.Category_Repository import Category_Repository
from repository.ObjectRepository import ObjectRepository
from repository.LoanRepository import LoanRepository


class ExportService:

    def __init__(self):
        self.friend_repository = FriendRepositoryDB()
        self.category_repository = Category_Repository()
        self.object_repository = ObjectRepository()
        self.loan_repository = LoanRepository()
        
        # Create exports directory if it doesn't exist
        self.export_dir = "exports"
        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir)

    def _get_timestamp(self):
        """Get current timestamp for file naming"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def export_friends_to_csv(self):
        """Export all friends to CSV"""
        try:
            friends = self.friend_repository.select_friends()
            if not friends:
                print("No hay amigos para exportar")
                return None

            filename = f"{self.export_dir}/amigos_{self._get_timestamp()}.csv"
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['ID', 'Nombre', 'Telefono', 'Email', 'Direccion', 'Rol']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for friend in friends:
                    writer.writerow({
                        'ID': friend.id,
                        'Nombre': friend.name,
                        'Telefono': friend.phone,
                        'Email': friend.mail,
                        'Direccion': friend.adress,
                        'Rol': friend.rol
                    })
            
            print(f"✓ Amigos exportados a: {filename}")
            return filename
            
        except Exception as e:
            print(f"Error exportando amigos: {e}")
            return None

    def export_categories_to_csv(self):
        """Export all categories to CSV"""
        try:
            categories = self.category_repository.select_categories()
            if not categories:
                print("No hay categorías para exportar")
                return None

            filename = f"{self.export_dir}/categorias_{self._get_timestamp()}.csv"
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['ID', 'Descripcion']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for category in categories:
                    writer.writerow({
                        'ID': category.id_category,
                        'Descripcion': category.description
                    })
            
            print(f"✓ Categorías exportadas a: {filename}")
            return filename
            
        except Exception as e:
            print(f"Error exportando categorías: {e}")
            return None

    def export_objects_to_csv(self):
        """Export all objects to CSV"""
        try:
            objects = self.object_repository.select_objects()
            if not objects:
                print("No hay objetos para exportar")
                return None

            filename = f"{self.export_dir}/objetos_{self._get_timestamp()}.csv"
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['ID', 'Descripcion', 'Estado', 'Categoria_ID', 'Categoria_Nombre']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for obj in objects:
                    # Convert state to Spanish
                    state_display = "Disponible" if obj.state == "available" else "Reservado" if obj.state == "loaned" else obj.state
                    
                    writer.writerow({
                        'ID': obj.id_object,
                        'Descripcion': obj.description,
                        'Estado': state_display,
                        'Categoria_ID': obj.category.id_category if obj.category else '',
                        'Categoria_Nombre': obj.category.description if obj.category else ''
                    })
            
            print(f"✓ Objetos exportados a: {filename}")
            return filename
            
        except Exception as e:
            print(f"Error exportando objetos: {e}")
            return None

    def export_loans_to_csv(self):
        """Export all loans to CSV"""
        try:
            loans = self.loan_repository.select_loans()
            if not loans:
                print("No hay préstamos para exportar")
                return None

            filename = f"{self.export_dir}/prestamos_{self._get_timestamp()}.csv"
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['ID', 'Fecha_Prestamo', 'Fecha_Devolucion', 'Estado', 
                             'Amigo_ID', 'Amigo_Nombre', 'Objeto_ID', 'Objeto_Descripcion']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for loan in loans:
                    # Convert state to Spanish
                    state_map = {
                        'active': 'Activo',
                        'returned': 'Retornado',
                        'overdue': 'Vencido'
                    }
                    state_display = state_map.get(loan.state, loan.state)
                    
                    writer.writerow({
                        'ID': loan.id_loan,
                        'Fecha_Prestamo': loan.date_loan,
                        'Fecha_Devolucion': loan.date_return,
                        'Estado': state_display,
                        'Amigo_ID': loan.friend.id if loan.friend else '',
                        'Amigo_Nombre': loan.friend.name if loan.friend else '',
                        'Objeto_ID': loan.object.id_object if loan.object else '',
                        'Objeto_Descripcion': loan.object.description if loan.object else ''
                    })
            
            print(f"✓ Préstamos exportados a: {filename}")
            return filename
            
        except Exception as e:
            print(f"Error exportando préstamos: {e}")
            return None

    def export_all_to_csv(self):
        """Export all data to separate CSV files"""
        print("\n=== EXPORTANDO TODA LA BASE DE DATOS ===")
        
        exported_files = []
        
        # Export each table
        files = [
            self.export_friends_to_csv(),
            self.export_categories_to_csv(),
            self.export_objects_to_csv(),
            self.export_loans_to_csv()
        ]
        
        exported_files = [f for f in files if f is not None]
        
        if exported_files:
            print(f"\n✓ Exportación completada. {len(exported_files)} archivos creados:")
            for file in exported_files:
                print(f"  - {file}")
            
            # Create a summary file
            summary_filename = f"{self.export_dir}/resumen_exportacion_{self._get_timestamp()}.txt"
            with open(summary_filename, 'w', encoding='utf-8') as summary_file:
                summary_file.write("RESUMEN DE EXPORTACIÓN\n")
                summary_file.write("=" * 50 + "\n")
                summary_file.write(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                summary_file.write(f"Archivos exportados: {len(exported_files)}\n\n")
                
                for file in exported_files:
                    summary_file.write(f"- {file}\n")
                
                summary_file.write(f"\nTodos los archivos están en la carpeta: {self.export_dir}/\n")
            
            print(f"  - {summary_filename}")
            return exported_files
        else:
            print("No se pudo exportar ningún archivo")
            return []

    def export_custom_report(self):
        """Export a custom report with combined data"""
        try:
            print("\n=== REPORTE PERSONALIZADO ===")
            
            filename = f"{self.export_dir}/reporte_completo_{self._get_timestamp()}.csv"
            
            # Get loans with all related data
            loans = self.loan_repository.select_loans()
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'Prestamo_ID', 'Fecha_Prestamo', 'Fecha_Devolucion', 'Estado_Prestamo',
                    'Dias_Prestado', 'Amigo_ID', 'Amigo_Nombre', 'Amigo_Email', 'Amigo_Telefono',
                    'Objeto_ID', 'Objeto_Descripcion', 'Objeto_Estado', 'Categoria_Nombre'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                
                for loan in loans:
                    # Calculate days loaned
                    if loan.date_return and loan.date_loan:
                        if loan.state == 'returned':
                            days_loaned = (loan.date_return - loan.date_loan).days
                        else:
                            days_loaned = (datetime.now().date() - loan.date_loan).days
                    else:
                        days_loaned = ''
                    
                    # Convert states to Spanish
                    loan_state = {
                        'active': 'Activo',
                        'returned': 'Retornado',
                        'overdue': 'Vencido'
                    }.get(loan.state, loan.state)
                    
                    object_state = "Disponible" if loan.object and loan.object.state == "available" else "Reservado"
                    
                    writer.writerow({
                        'Prestamo_ID': loan.id_loan,
                        'Fecha_Prestamo': loan.date_loan,
                        'Fecha_Devolucion': loan.date_return,
                        'Estado_Prestamo': loan_state,
                        'Dias_Prestado': days_loaned,
                        'Amigo_ID': loan.friend.id if loan.friend else '',
                        'Amigo_Nombre': loan.friend.name if loan.friend else '',
                        'Amigo_Email': loan.friend.mail if loan.friend else '',
                        'Amigo_Telefono': loan.friend.phone if loan.friend else '',
                        'Objeto_ID': loan.object.id_object if loan.object else '',
                        'Objeto_Descripcion': loan.object.description if loan.object else '',
                        'Objeto_Estado': object_state,
                        'Categoria_Nombre': loan.object.category.description if loan.object and loan.object.category else ''
                    })
            
            print(f"✓ Reporte personalizado exportado a: {filename}")
            return filename
            
        except Exception as e:
            print(f"Error creando reporte personalizado: {e}")
            return None