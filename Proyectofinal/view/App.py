from domain.Friend import Friend
from repository.FriendRepository import FriendRepository
from service.FriendService import FriendService
from repository.FriendRepositoryDB import FriendRepositoryDB
from service.Category_Service import Category_Service
from service.ObjectService import ObjectService
from service.LoanService import LoanService
from service.ExportService import ExportService


class App:

    def __init__(self):
        self.friendRepository = FriendRepository()
        self.friendRepositoryDB = FriendRepositoryDB()
        self.friendService = FriendService()
        self.categoryService = Category_Service()
        self.objectService = ObjectService()
        self.loanService = LoanService()
        self.exportService = ExportService()
        self.friend = Friend(None, None, None, None, None, None)

    def run_app(self):
        print("=== SISTEMA DE GESTIÓN DE PRÉSTAMOS ===")
        init = int(input("Ingrese 1 para inicializar la aplicacion: "))
        
        while init != 0:
            print("\n" + "="*50)
            print("           MENÚ PRINCIPAL")
            print("="*50)
            option = int(input(
                "1. Gestionar Amigos\n"
                "2. Gestionar Categorías\n"
                "3. Gestionar Objetos\n"
                "4. Gestionar Préstamos\n"
                "5. Exportar Datos a CSV\n"
                "0. Salir\n"
                "Seleccione una opción: "
            ))
            
            match option:
                case 1:
                    self.menu_friend()
                case 2:
                    self.menu_category()
                case 3:
                    self.menu_object()
                case 4:
                    self.menu_loan()
                case 5:
                    self.menu_export()
                case 0:
                    print("¡Gracias por usar el sistema!")
                    init = 0
                case _:
                    print("Seleccione una opción válida")

    def menu_friend(self):
        while True:
            print("\n" + "="*40)
            print("        GESTIÓN DE AMIGOS")
            print("="*40)
            option = int(input(
                "1. Crear Amigo\n"
                "2. Listar Amigos\n"
                "3. Buscar Amigo por ID\n"
                "4. Actualizar Amigo\n"
                "5. Eliminar Amigo\n"
                "0. Volver al Menú Principal\n"
                "Seleccione una opción: "
            ))
            
            match option:
                case 1:
                    self.friendService.createUser()
                case 2:
                    friends = self.friendService.selectUser()
                    if friends:
                        print("\n=== LISTA DE AMIGOS ===")
                        for friend in friends:
                            print(friend)
                    else:
                        print("No hay amigos registrados")
                case 3:
                    id_friend = int(input("Ingrese el ID del amigo: "))
                    friend = self.friendService.select_friend_by_id(id_friend)
                    if friend:
                        print(f"Amigo encontrado: {friend}")
                    else:
                        print("Amigo no encontrado")
                case 4:
                    self.friendService.update_friend()
                case 5:
                    id_friend = int(input("Ingrese el ID del amigo a eliminar: "))
                    friend = self.friendService.select_friend_by_id(id_friend)
                    if friend:
                        print(f"Amigo a eliminar: {friend}")
                        confirm = input("¿Está seguro? (s/n): ")
                        if confirm.lower() == 's':
                            self.friendService.removeFriend(id_friend)
                            print("Amigo eliminado exitosamente")
                        else:
                            print("Operación cancelada")
                    else:
                        print("Amigo no encontrado")
                case 0:
                    break
                case _:
                    print("Seleccione una opción válida")

    def menu_category(self):
        while True:
            print("\n" + "="*40)
            print("      GESTIÓN DE CATEGORÍAS")
            print("="*40)
            option = int(input(
                "1. Crear Categoría\n"
                "2. Listar Categorías\n"
                "3. Buscar Categoría por ID\n"
                "4. Actualizar Categoría\n"
                "5. Eliminar Categoría\n"
                "0. Volver al Menú Principal\n"
                "Seleccione una opción: "
            ))
            
            match option:
                case 1:
                    self.categoryService.create_category()
                case 2:
                    self.categoryService.list_categories()
                case 3:
                    category = self.categoryService.select_category_by_id()
                    if category:
                        print(f"Categoría encontrada: {category}")
                case 4:
                    self.categoryService.update_category()
                case 5:
                    self.categoryService.delete_category()
                case 0:
                    break
                case _:
                    print("Seleccione una opción válida")

    def menu_object(self):
        while True:
            print("\n" + "="*40)
            print("       GESTIÓN DE OBJETOS")
            print("="*40)
            option = int(input(
                "1. Crear Objeto\n"
                "2. Listar Todos los Objetos\n"
                "3. Buscar Objeto por ID\n"
                "4. Actualizar Objeto\n"
                "5. Eliminar Objeto\n"
                "6. Listar Objetos por Categoría\n"
                "7. Listar Objetos Disponibles\n"
                "0. Volver al Menú Principal\n"
                "Seleccione una opción: "
            ))
            
            match option:
                case 1:
                    self.objectService.create_object()
                case 2:
                    self.objectService.list_objects()
                case 3:
                    obj = self.objectService.select_object_by_id()
                    if obj:
                        print(f"Objeto encontrado: {obj}")
                case 4:
                    self.objectService.update_object()
                case 5:
                    self.objectService.delete_object()
                case 6:
                    self.objectService.list_objects_by_category()
                case 7:
                    self.objectService.list_available_objects()
                case 0:
                    break
                case _:
                    print("Seleccione una opción válida")

    def menu_loan(self):
        while True:
            print("\n" + "="*40)
            print("       GESTIÓN DE PRÉSTAMOS")
            print("="*40)
            option = int(input(
                "1. Crear Préstamo\n"
                "2. Listar Todos los Préstamos\n"
                "3. Buscar Préstamo por ID\n"
                "4. Devolver Préstamo\n"
                "5. Actualizar Préstamo\n"
                "6. Eliminar Préstamo\n"
                "7. Listar Préstamos Activos\n"
                "8. Listar Préstamos por Amigo\n"
                "9. Verificar Préstamos Vencidos\n"
                "0. Volver al Menú Principal\n"
                "Seleccione una opción: "
            ))
            
            match option:
                case 1:
                    self.loanService.create_loan()
                case 2:
                    self.loanService.list_loans()
                case 3:
                    loan = self.loanService.select_loan_by_id()
                    if loan:
                        friend_name = loan.friend.name if loan.friend else "N/A"
                        object_desc = loan.object.description if loan.object else "N/A"
                        print(f"Préstamo encontrado: ID: {loan.id_loan}, Amigo: {friend_name}, Objeto: {object_desc}")
                case 4:
                    self.loanService.return_loan()
                case 5:
                    self.loanService.update_loan()
                case 6:
                    self.loanService.delete_loan()
                case 7:
                    self.loanService.list_active_loans()
                case 8:
                    self.loanService.list_loans_by_friend()
                case 9:
                    self.loanService.check_overdue_loans()
                case 0:
                    break
                case _:
                    print("Seleccione una opción válida")

    def menu_export(self):
        try:
            export_service = ExportService()
            
            print("\n===== MENÚ DE EXPORTACIÓN =====")
            print("1. Exportar Amigos")
            print("2. Exportar Categorías")
            print("3. Exportar Objetos")
            print("4. Exportar Préstamos")
            print("5. Exportar Todos los Datos")
            print("0. Volver al menú principal")
            
            option = int(input("Seleccione una opción: "))
            
            match option:
                case 1:
                    path = export_service.export_friends_to_csv()
                    if path:
                        print(f"✓ Amigos exportados exitosamente a: {path}")
                case 2:
                    path = export_service.export_categories_to_csv()
                    if path:
                        print(f"✓ Categorías exportadas exitosamente a: {path}")
                case 3:
                    path = export_service.export_objects_to_csv()
                    if path:
                        print(f"✓ Objetos exportados exitosamente a: {path}")
                case 4:
                    path = export_service.export_loans_to_csv()
                    if path:
                        print(f"✓ Préstamos exportados exitosamente a: {path}")
                case 5:
                    path = export_service.export_all_to_csv()
                    if path:
                        print(f"✓ Todos los datos exportados exitosamente a: {path}")
                case 0:
                    print("Volviendo al menú principal...")
                case _:
                    print("Seleccione una opción válida")
                    
        except ValueError:
            print("Por favor ingrese un número válido")
        except Exception as e:
            print(f"Error durante la exportación: {e}")

    