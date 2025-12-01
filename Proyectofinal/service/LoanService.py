from domain.loan import Loan
from domain.Friend import Friend
from domain.object import Object
from repository.LoanRepository import LoanRepository
from repository.FriendRepositoryDB import FriendRepositoryDB
from repository.ObjectRepository import ObjectRepository
from utils.Validators import Validators
from datetime import date, datetime


class LoanService:

    def __init__(self):
        self.loan = Loan(None, None, None, None, None, None)
        self.loan_repository = LoanRepository()
        self.friend_repository = FriendRepositoryDB()
        self.object_repository = ObjectRepository()

    def _get_state_display(self, state):
        """Convert database state to Spanish display"""
        state_map = {
            'active': 'Activo',
            'returned': 'Retornado',
            'overdue': 'Vencido'
        }
        return state_map.get(state, state)

    def create_loan(self):
        print("\n=== CREAR NUEVO PRÉSTAMO ===")
        
        # Show available objects
        available_objects = self.object_repository.select_available_objects()
        if not available_objects:
            print("❌ No hay objetos disponibles para prestar")
            return
        
        print("Objetos disponibles:")
        for obj in available_objects:
            print(f"ID: {obj.id_object}, Descripción: {obj.description}, Estado: {obj.state}")
        
        # Show friends
        friends = self.friend_repository.select_friends()
        if not friends:
            print("❌ No hay amigos registrados")
            return
        
        print("\nAmigos disponibles:")
        for friend in friends:
            print(f"ID: {friend.id}, Nombre: {friend.name}, Email: {friend.mail}")
        
        # Get loan details with validation
        # Validar selección de objeto
        object_ids = [obj.id_object for obj in available_objects]
        object_id_str = Validators.get_validated_input(
            "Ingrese el ID del objeto a prestar: ", 
            Validators.validate_choice, 
            object_ids
        )
        object_id = int(object_id_str)
        
        # Validar selección de amigo
        friend_ids = [friend.id for friend in friends]
        friend_id_str = Validators.get_validated_input(
            "Ingrese el ID del amigo: ", 
            Validators.validate_choice, 
            friend_ids
        )
        friend_id = int(friend_id_str)
        
        # Validar fecha de devolución
        return_date_str = Validators.get_validated_input(
            "Ingrese la fecha de devolución esperada (YYYY-MM-DD): ", 
            Validators.validate_future_date
        )
        
        # Validate object and friend
        obj = self.object_repository.select_object_by_id(object_id)
        friend = self.friend_repository.select_user_by_id(friend_id)
        
        if not obj:
            print("Objeto no encontrado")
            return
        
        if not friend:
            print("Amigo no encontrado")
            return
        
        if obj.state != 'available':
            print("❌ El objeto no está disponible para prestar")
            return
        
        # Validar fecha de préstamo
        loan_date_str = input("Fecha de préstamo (YYYY-MM-DD) o presione Enter para hoy: ").strip()
        if not loan_date_str:
            loan_date = date.today()
        else:
            is_valid, message = Validators.validate_date(loan_date_str)
            if not is_valid:
                print(f"❌ Error en fecha de préstamo: {message}")
                return
            loan_date = datetime.strptime(loan_date_str, '%Y-%m-%d').date()
        
        # Convertir la fecha de devolución validada
        try:
            return_date = datetime.strptime(return_date_str, '%Y-%m-%d').date()
        except ValueError:
            print("❌ Error en formato de fecha de devolución")
            return
        
        # Create loan
        try:
            self.loan = Loan(None, loan_date, return_date, friend, obj, 'active')
            self.loan_repository.create_loan_db(self.loan)
            print("✅ Préstamo creado exitosamente")
        except Exception as e:
            print(f"❌ Error al crear el préstamo: {e}")

    def select_loans(self):
        return self.loan_repository.select_loans()

    def select_loan_by_id(self):
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID del préstamo: ", 
            Validators.validate_id, 
            "ID del préstamo"
        )
        id_loan = int(id_str)
        
        loan = self.loan_repository.select_loan_by_id(id_loan)
        if not loan:
            print("❌ Préstamo no encontrado")
        return loan

    def return_loan(self):
        print("\n=== DEVOLVER PRESTAMO ===")
        
        # Show active loans
        active_loans = self.loan_repository.select_active_loans()
        if not active_loans:
            print("No hay prestamos activos")
            return
        
        print("Préstamos activos:")
        for loan in active_loans:
            print(f"ID: {loan.id_loan}, Amigo: {loan.friend.name if loan.friend else 'N/A'}, "
                  f"Objeto: {loan.object.description if loan.object else 'N/A'}, "
                  f"Fecha préstamo: {loan.date_loan}")
        
        # Validar ID del préstamo
        loan_ids = [loan.id_loan for loan in active_loans]
        id_str = Validators.get_validated_input(
            "Ingrese el ID del préstamo a devolver: ", 
            Validators.validate_choice, 
            loan_ids
        )
        id_loan = int(id_str)
        
        try:
            if self.loan_repository.return_loan(id_loan):
                print("✅ Préstamo marcado como devuelto exitosamente")
            else:
                print("❌ Error al devolver el préstamo")
        except Exception as e:
            print(f"❌ Error al devolver el préstamo: {e}")

    def update_loan(self):
        print("\n=== ACTUALIZAR PRÉSTAMO ===")
        
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID del préstamo a modificar: ", 
            Validators.validate_id, 
            "ID del préstamo"
        )
        id_loan = int(id_str)
        
        loan = self.loan_repository.select_loan_by_id(id_loan)
        
        if loan:
            print(f"Préstamo actual: {loan}")
            
            # Update return date
            new_return_date = input(f"Nueva fecha de devolución (actual: {loan.date_return}) (YYYY-MM-DD): ").strip()
            if new_return_date:
                is_valid, message = Validators.validate_future_date(new_return_date)
                if not is_valid:
                    print(f"❌ Error en la fecha: {message}")
                    return
                loan.date_return = datetime.strptime(new_return_date, '%Y-%m-%d').date()
            
            # Update state
            current_state_display = self._get_state_display(loan.state)
            
            print(f"\nEstado actual: {current_state_display}")
            print("Estados disponibles:")
            print("1. Activo")
            print("2. Retornado")
            print("3. Vencido")
            print("4. Mantener estado actual")
            
            state_option = input("Seleccione el nuevo estado (1, 2, 3 o 4): ")
            
            if state_option == "1":
                loan.state = "active"
            elif state_option == "2":
                loan.state = "returned"
            elif state_option == "3":
                loan.state = "overdue"
            elif state_option == "4":
                # Keep current state
                pass
            else:
                print("Opción inválida, manteniendo estado actual")
            
            try:
                self.loan_repository.update_loan(loan)
                print("✅ Préstamo actualizado exitosamente")
            except Exception as e:
                print(f"❌ Error al actualizar el préstamo: {e}")
        else:
            print("❌ Préstamo no encontrado")

    def delete_loan(self):
        print("\n=== ELIMINAR PRÉSTAMO ===")
        
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID del préstamo a eliminar: ", 
            Validators.validate_id, 
            "ID del préstamo"
        )
        id_loan = int(id_str)
        
        loan = self.loan_repository.select_loan_by_id(id_loan)
        
        if loan:
            print(f"Préstamo a eliminar: {loan}")
            
            # Confirmar eliminación
            confirm = input("¿Está seguro de eliminar este préstamo? (s/n): ").strip().lower()
            if confirm == 's' or confirm == 'si':
                try:
                    self.loan_repository.delete_loan_by_id(id_loan)
                    print("✅ Préstamo eliminado exitosamente")
                except Exception as e:
                    print(f"❌ Error al eliminar el préstamo: {e}")
            else:
                print("Operación cancelada")
        else:
            print("❌ Préstamo no encontrado")

    def list_loans(self):
        loans = self.select_loans()
        if loans:
            print("\n=== LISTA DE PRESTAMOS ===")
            for loan in loans:
                friend_name = loan.friend.name if loan.friend else "N/A"
                object_desc = loan.object.description if loan.object else "N/A"
                state_display = self._get_state_display(loan.state)
                print(f"ID: {loan.id_loan}, Amigo: {friend_name}, Objeto: {object_desc}, "
                      f"Fecha prestamo: {loan.date_loan}, Fecha devolucion: {loan.date_return}, Estado: {state_display}")
        else:
            print("No hay prestamos registrados")

    def list_active_loans(self):
        loans = self.loan_repository.select_active_loans()
        if loans:
            print("\n=== PRESTAMOS ACTIVOS ===")
            for loan in loans:
                friend_name = loan.friend.name if loan.friend else "N/A"
                object_desc = loan.object.description if loan.object else "N/A"
                print(f"ID: {loan.id_loan}, Amigo: {friend_name}, Objeto: {object_desc}, "
                      f"Fecha prestamo: {loan.date_loan}, Fecha devolucion esperada: {loan.date_return}")
        else:
            print("No hay prestamos activos")

    def list_loans_by_friend(self):
        print("\n=== PRESTAMOS POR AMIGO ===")
        
        # Show friends
        friends = self.friend_repository.select_friends()
        if not friends:
            print("No hay amigos registrados")
            return
        
        print("Amigos disponibles:")
        for friend in friends:
            print(f"ID: {friend.id}, Nombre: {friend.name}")
        
        # Validar ID del amigo
        friend_ids = [friend.id for friend in friends]
        friend_id_str = Validators.get_validated_input(
            "Ingrese el ID del amigo: ", 
            Validators.validate_choice, 
            friend_ids
        )
        friend_id = int(friend_id_str)
        
        loans = self.loan_repository.select_loans_by_friend(friend_id)
        
        if loans:
            print(f"\nPrestamos del amigo:")
            for loan in loans:
                object_desc = loan.object.description if loan.object else "N/A"
                state_display = self._get_state_display(loan.state)
                print(f"ID: {loan.id_loan}, Objeto: {object_desc}, "
                      f"Fecha prestamo: {loan.date_loan}, Fecha devolucion: {loan.date_return}, Estado: {state_display}")
        else:
            print("No hay prestamos para este amigo")

    def check_overdue_loans(self):
        """Check for overdue loans"""
        active_loans = self.loan_repository.select_active_loans()
        today = date.today()
        overdue_loans = []
        
        for loan in active_loans:
            if loan.date_return and loan.date_return < today:
                overdue_loans.append(loan)
        
        if overdue_loans:
            print("\n=== PRESTAMOS VENCIDOS ===")
            for loan in overdue_loans:
                friend_name = loan.friend.name if loan.friend else "N/A"
                object_desc = loan.object.description if loan.object else "N/A"
                days_overdue = (today - loan.date_return).days
                print(f"ID: {loan.id_loan}, Amigo: {friend_name}, Objeto: {object_desc}, "
                      f"Fecha devolucion: {loan.date_return}, Dias vencido: {days_overdue}")
        else:
            print("No hay prestamos vencidos")