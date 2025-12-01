from domain.object import Object
from domain.Category import Category
from repository.ObjectRepository import ObjectRepository
from repository.Category_Repository import Category_Repository
from utils.Validators import Validators


class ObjectService:

    def __init__(self):
        self.object = Object(None, None, None, None)
        self.object_repository = ObjectRepository()
        self.category_repository = Category_Repository()

    def create_object(self):
        print("\n=== CREAR NUEVO OBJETO ===")
        
        # Show available categories
        categories = self.category_repository.select_categories()
        if not categories:
            print("❌ No hay categorías disponibles. Debe crear una categoría primero.")
            return
        
        print("Categorías disponibles:")
        for cat in categories:
            print(f"ID: {cat.id_category}, Descripción: {cat.description}")
        
        # Validar descripción
        description = Validators.get_validated_input(
            "Ingrese la descripción del objeto: ", 
            Validators.validate_description
        )
        
        print("\nEstados disponibles:")
        print("1. Disponible")
        print("2. Reservado")
        
        # Validar estado
        state_option = Validators.get_validated_input(
            "Seleccione el estado (1 o 2): ", 
            Validators.validate_choice, 
            [1, 2]
        )
        
        # Map user input to database values
        if state_option == "1":
            state = "available"
        else:
            state = "loaned"
        
        # Validar categoría
        category_ids = [cat.id_category for cat in categories]
        category_id_str = Validators.get_validated_input(
            "Ingrese el ID de la categoría: ", 
            Validators.validate_choice, 
            category_ids
        )
        category_id = int(category_id_str)
        
        # Validate category
        category = self.category_repository.select_category_by_id(category_id)
        if not category:
            print("❌ Categoría no encontrada")
            return
        
        self.object = Object(None, description, state, category)

        
        try:
            self.object_repository.create_object_db(self.object)
            print("✅ Objeto creado exitosamente")
        except Exception as e:
            print(f"❌ Error al crear el objeto: {e}")

    def select_objects(self):
        return self.object_repository.select_objects()

    def select_object_by_id(self):
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID del objeto: ", 
            Validators.validate_id, 
            "ID del objeto"
        )
        id_object = int(id_str)
        
        obj = self.object_repository.select_object_by_id(id_object)
        if not obj:
            print("❌ Objeto no encontrado")
        return obj

    def update_object(self):
        print("\n=== ACTUALIZAR OBJETO ===")
        
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID del objeto a modificar: ", 
            Validators.validate_id, 
            "ID del objeto"
        )
        id_object = int(id_str)
        
        obj = self.object_repository.select_object_by_id(id_object)
        
        if obj:
            print(f"Objeto actual: {obj}")
            print("\nDeje en blanco para mantener el valor actual:")
            
            # Validar nueva descripción si se proporciona
            new_description = input(f"Nueva descripción (actual: {obj.description}): ").strip()
            if new_description:
                is_valid, message = Validators.validate_description(new_description)
                if not is_valid:
                    print(f"❌ Error en la descripción: {message}")
                    return
                obj.description = new_description
            
            # Show current state in user-friendly format
            current_state_display = "Disponible" if obj.state == "available" else "Reservado" if obj.state == "loaned" else obj.state
            print(f"\nEstado actual: {current_state_display}")
            print("Estados disponibles:")
            print("1. Disponible")
            print("2. Reservado")
            print("3. Mantener estado actual")
            
            state_option = input("Seleccione el nuevo estado (1, 2 o 3): ")
            
            if state_option == "1":
                new_state = "available"
            elif state_option == "2":
                new_state = "loaned"
            elif state_option == "3":
                new_state = obj.state
            else:
                print("Opción inválida, manteniendo estado actual")
                new_state = obj.state
            
            # Show categories
            categories = self.category_repository.select_categories()
            print("Categorias disponibles:")
            for cat in categories:
                print(f"ID: {cat.id_category}, Descripcion: {cat.description}")
            
            category_input = input(f"Nueva categoria ID (actual: {obj.category.id_category if obj.category else 'None'}): ").strip()
            
            if category_input:
                # Validar que el ID de categoría sea válido
                category_ids = [cat.id_category for cat in categories]
                try:
                    category_id = int(category_input)
                    if category_id not in category_ids:
                        print("❌ ID de categoría no válido")
                        return
                    category = self.category_repository.select_category_by_id(category_id)
                    if not category:
                        print("❌ Categoría no encontrada")
                        return
                except ValueError:
                    print("❌ El ID debe ser un número entero")
                    return
            else:
                category = obj.category
            
            # Update object
            if new_description:
                obj.description = new_description
            obj.state = new_state
            obj.category = category
            
            try:
                self.object_repository.update_object(obj)
                print("✅ Objeto actualizado exitosamente")
            except Exception as e:
                print(f"❌ Error al actualizar el objeto: {e}")
        else:
            print("Objeto no encontrado")

    def delete_object(self):
        print("\n=== ELIMINAR OBJETO ===")
        
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID del objeto a eliminar: ", 
            Validators.validate_id, 
            "ID del objeto"
        )
        id_object = int(id_str)
        
        obj = self.object_repository.select_object_by_id(id_object)
        
        if obj:
            print(f"Objeto a eliminar: {obj}")
            
            # Confirmar eliminación
            confirm = input("¿Está seguro de eliminar este objeto? (s/n): ").strip().lower()
            if confirm == 's' or confirm == 'si':
                try:
                    self.object_repository.delete_object_by_id(id_object)
                    print("✅ Objeto eliminado exitosamente")
                except Exception as e:
                    print(f"❌ Error al eliminar el objeto: {e}")
                    print("Puede que existan préstamos asociados a este objeto")
            else:
                print("Operación cancelada")
        else:
            print("❌ Objeto no encontrado")

    def list_objects(self):
        objects = self.select_objects()
        if objects:
            print("\n=== LISTA DE OBJETOS ===")
            for obj in objects:
                # Display user-friendly state
                state_display = "Disponible" if obj.state == "available" else "Reservado" if obj.state == "loaned" else obj.state
                category_name = obj.category.description if obj.category else "Sin categoría"
                print(f"ID: {obj.id_object}, Descripción: {obj.description}, Estado: {state_display}, Categoría: {category_name}")
        else:
            print("No hay objetos registrados")

    def list_objects_by_category(self):
        print("\n=== OBJETOS POR CATEGORIA ===")
        
        # Show categories
        categories = self.category_repository.select_categories()
        if not categories:
            print("No hay categorias disponibles")
            return
        
        print("Categorias disponibles:")
        for cat in categories:
            print(f"ID: {cat.id_category}, Descripcion: {cat.description}")
        
        # Validar ID de categoría
        category_ids = [cat.id_category for cat in categories]
        category_id_str = Validators.get_validated_input(
            "Ingrese el ID de la categoría: ", 
            Validators.validate_choice, 
            category_ids
        )
        category_id = int(category_id_str)
        
        objects = self.object_repository.select_objects_by_category(category_id)
        
        if objects:
            print(f"\nObjetos en la categoria:")
            for obj in objects:
                state_display = "Disponible" if obj.state == "available" else "Reservado" if obj.state == "loaned" else obj.state
                category_name = obj.category.description if obj.category else "Sin categoría"
                print(f"ID: {obj.id_object}, Descripción: {obj.description}, Estado: {state_display}, Categoría: {category_name}")
        else:
            print("No hay objetos en esta categoria")

    def list_available_objects(self):
        objects = self.object_repository.select_available_objects()
        if objects:
            print("\n=== OBJETOS DISPONIBLES ===")
            for obj in objects:
                category_name = obj.category.description if obj.category else "Sin categoría"
                print(f"ID: {obj.id_object}, Descripción: {obj.description}, Estado: Disponible, Categoría: {category_name}")
        else:
            print("No hay objetos disponibles")