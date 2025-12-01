from repository.Conexion import conexion
from domain.Category import Category

class Category_Repository:


    def __init__(self,):
        self.db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        self.db.connect()


    def create_category_db(self, category):
        query = "INSERT INTO category (description) VALUES (%s)"
        values = (category.description,)
        self.db.execute_query(query, values)

    def select_categories(self):
        query = "SELECT * FROM category"
        result = self.db.execute_query(query)
        if result:
            category_list = []
            for row in result:
                category = Category.from_row(row)
                category_list.append(category)
            return category_list
        else:
            print("No categories found")
            return []

    def select_category_by_id(self, id_category):
        query = "SELECT * FROM category WHERE id_category=%s"
        result = self.db.execute_query(query, (id_category,))
        if result:
            return Category.from_row(result[0])
        else:
            print("Category not found")
            return None

    def update_category(self, category):
        query = "UPDATE category SET description=%s WHERE id_category=%s"
        values = (category.description, category.id_category)
        self.db.execute_query(query, values)

    def delete_category_by_id(self, id_category):
        query = "DELETE FROM category WHERE id_category=%s"
        self.db.execute_query(query, (id_category,))

