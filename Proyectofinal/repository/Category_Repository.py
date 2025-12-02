
# Importamos la clase 'conexion' para manejar la conexión a la base de datos#_Repository:

    # Constructor de la clase
    def __init__(self):
        # Creamos una instancia de la conexión a la base de datos con los parámetros necesarios
        self.db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        # Establecemos la conexión con la base de datos
        self.db.connect()

    # Método para crear una nueva categoría en la base de datos
    def create_category_db(self, category):
        # Consulta SQL para insertar una nueva categoría
        query = "INSERT INTO category (description) VALUES (%s)"
        # Valores que se insertarán (solo la descripción de la categoría)
        values = (category.description,)
        # Ejecutamos la consulta con los valores
        self.db.execute_query(query, values)

    # Método para obtener todas las categorías de la base de datos
    def select_categories(self):
        # Consulta SQL para seleccionar todas las categorías
        query = "SELECT * FROM category"
        # Ejecutamos la consulta y guardamos el resultado
        result = self.db.execute_query(query)
        # Si hay resultados
        if result:
            category_list = []  # Lista para almacenar las categorías
            # Recorremos cada fila del resultado
            for row in result:
                # Convertimos la fila en un objeto 'Category' usando el método 'from_row'
                category = Category.from_row(row)
                # Agregamos el objeto a la lista
                category_list.append(category)
            # Retornamos la lista de categorías
            return category_list
        else:
            # Si no hay categorías, mostramos un mensaje y retornamos lista vacía
            print("No categories found")
            return []

    # Método para obtener una categoría por su ID
    def select_category_by_id(self, id_category):
        # Consulta SQL para seleccionar una categoría específica por ID
        query = "SELECT * FROM category WHERE id_category=%s"
        # Ejecutamos la consulta con el ID como parámetro
        result = self.db.execute_query(query, (id_category,))
        # Si encontramos resultados
        if result:
            # Retornamos la primera fila convertida en objeto 'Category'
            return Category.from_row(result[0])
        else:
            # Si no se encuentra la categoría, mostramos mensaje y retornamos None
            print("Category not found")
            return None

    # Método para actualizar una categoría existente
    def update_category(self, category):
        # Consulta SQL para actualizar la descripción de la categoría según su ID
        query = "UPDATE category SET description=%s WHERE id_category=%s"
        # Valores que se actualizarán (nueva descripción y el ID)
        values = (category.description, category.id_category)
        # Ejecutamos la consulta con los valores
        self.db.execute_query(query, values)

    # Método para eliminar una categoría por su ID
    def delete_category_by_id(self, id_category):
        # Consulta SQL para eliminar la categoría según su ID
        query = "DELETE FROM category WHERE id_category=%s"
        # Ejecutamos la consulta con el ID como parámetro
        self.db.execute_query(query, (id_category,))

from repository.Conexion import conexion

# Importamos la clase 'Category' que representa el modelo de categoría
from domain.Category import Category

# Definimos la clase 'Category_Repository' que se encargará de las operaciones CRUD sobre la tabla 'category'
