from repository.Conexion import conexion
from domain.object import Object
from domain.Category import Category

class ObjectRepository:

    def __init__(self):
        self.db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        self.db.connect()

    def create_object_db(self, obj):
        query = "INSERT INTO object (description, state, category_id) VALUES (%s, %s, %s)"
        values = (
            obj.description,
            obj.state,
            obj.category.id_category if obj.category else None
        )
        self.db.execute_query(query, values)

    def select_objects(self):
        query = """
        SELECT o.id_object, o.description, o.state, c.id_category, c.description as category_description
        FROM object o
        LEFT JOIN category c ON o.category_id = c.id_category
        """
        result = self.db.execute_query(query)
        if result:
            object_list = []
            for row in result:
                category = Category(row[3], row[4]) if row[3] else None
                obj = Object(row[0], row[1], row[2], category)
                object_list.append(obj)
            return object_list
        else:
            print("No objects found")
            return []

    def select_object_by_id(self, id_object):
        query = """
        SELECT o.id_object, o.description, o.state, c.id_category, c.description as category_description
        FROM object o
        LEFT JOIN category c ON o.category_id = c.id_category
        WHERE o.id_object = %s
        """
        result = self.db.execute_query(query, (id_object,))
        if result:
            row = result[0]
            category = Category(row[3], row[4]) if row[3] else None
            return Object(row[0], row[1], row[2], category)
        else:
            print("Object not found")
            return None

    def update_object(self, obj):
        query = "UPDATE object SET description=%s, state=%s, category_id=%s WHERE id_object=%s"
        values = (
            obj.description,
            obj.state,
            obj.category.id_category if obj.category else None,
            obj.id_object
        )
        self.db.execute_query(query, values)

    def delete_object_by_id(self, id_object):
        query = "DELETE FROM object WHERE id_object=%s"
        self.db.execute_query(query, (id_object,))

    def select_objects_by_category(self, category_id):
        query = """
        SELECT o.id_object, o.description, o.state, c.id_category, c.description as category_description
        FROM object o
        LEFT JOIN category c ON o.category_id = c.id_category
        WHERE o.category_id = %s
        """
        result = self.db.execute_query(query, (category_id,))
        if result:
            object_list = []
            for row in result:
                category = Category(row[3], row[4]) if row[3] else None
                obj = Object(row[0], row[1], row[2], category)
                object_list.append(obj)
            return object_list
        else:
            print("No objects found for this category")
            return []

    def select_available_objects(self):
        """Select objects that are available (not currently loaned)"""
        query = """
        SELECT o.id_object, o.description, o.state, c.id_category, c.description as category_description
        FROM object o
        LEFT JOIN category c ON o.category_id = c.id_category
        WHERE o.state = 'available'
        """
        result = self.db.execute_query(query)
        if result:
            object_list = []
            for row in result:
                category = Category(row[3], row[4]) if row[3] else None
                obj = Object(row[0], row[1], row[2], category)
                object_list.append(obj)
            return object_list
        else:
            print("No available objects found")
            return []