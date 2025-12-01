from domain.Category import Category
from repository.Category_Repository import Category_Repository
from utils.Validators import Validators


class Category_Service:

    def __init__(self):
        self.category = Category(None, None)
        self.category_repository = Category_Repository()

    def create_category(self):
        print("\n=== CREAR NUEVA CATEGORÍA ===")
        
        # Validar nombre de categoría
        description = Validators.get_validated_input(
            "Ingrese el nombre de la categoría: ", 
            Validators.validate_name, 
            "Nombre de categoría"
        )
        
        # Verificar si la categoría ya existe
        existing_categories = self.category_repository.select_categories()
        for category in existing_categories:
            if category.description.lower() == description.lower():
                print("❌ Error: Ya existe una categoría con este nombre")
                return
        
        self.category.description = description
        
        try:
            self.category_repository.create_category_db(self.category)
            print("✅ Categoría creada exitosamente")
        except Exception as e:
            print(f"❌ Error al crear la categoría: {e}")

    def select_categories(self):
        return self.category_repository.select_categories()

    def select_category_by_id(self):
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID de la categoría: ", 
            Validators.validate_id, 
            "ID de categoría"
        )
        id_category = int(id_str)
        
        category = self.category_repository.select_category_by_id(id_category)
        if not category:
            print("❌ Categoría no encontrada")
        return category

    def update_category(self):
        print("\n=== ACTUALIZAR CATEGORÍA ===")
        
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID de la categoría a modificar: ", 
            Validators.validate_id, 
            "ID de categoría"
        )
        id_category = int(id_str)
        
        category = self.category_repository.select_category_by_id(id_category)
        
        if category:
            print(f"Categoría actual: {category}")
            
            # Validar nueva descripción
            new_description = Validators.get_validated_input(
                "Ingrese el nuevo nombre de la categoría: ", 
                Validators.validate_name, 
                "Nombre de categoría"
            )
            
            # Verificar si ya existe otra categoría con ese nombre
            existing_categories = self.category_repository.select_categories()
            for existing_category in existing_categories:
                if existing_category.id_category != category.id_category and existing_category.description.lower() == new_description.lower():
                    print("❌ Error: Ya existe otra categoría con este nombre")
                    return
            
            category.description = new_description
            
            try:
                self.category_repository.update_category(category)
                print("✅ Categoría actualizada exitosamente")
            except Exception as e:
                print(f"❌ Error al actualizar la categoría: {e}")
        else:
            print("❌ Categoría no encontrada")

    def delete_category(self):
        print("\n=== ELIMINAR CATEGORÍA ===")
        
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID de la categoría a eliminar: ", 
            Validators.validate_id, 
            "ID de categoría"
        )
        id_category = int(id_str)
        
        category = self.category_repository.select_category_by_id(id_category)
        
        if category:
            print(f"Categoría a eliminar: {category}")
            
            # Confirmar eliminación
            confirm = input("¿Está seguro de eliminar esta categoría? (s/n): ").strip().lower()
            if confirm == 's' or confirm == 'si':
                try:
                    self.category_repository.delete_category_by_id(id_category)
                    print("✅ Categoría eliminada exitosamente")
                except Exception as e:
                    print(f"❌ Error al eliminar la categoría: {e}")
                    print("Puede que existan objetos asociados a esta categoría")
            else:
                print("Operación cancelada")
        else:
            print("❌ Categoría no encontrada")

    def list_categories(self):
        categories = self.select_categories()
        if categories:
            print("\n=== LISTA DE CATEGORIAS ===")
            for category in categories:
                print(category)
        else:
            print("No hay categorias registradas")
