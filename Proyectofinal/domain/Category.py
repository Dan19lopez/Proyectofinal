


class Category:


    def __init__(self, id_category, description):
        self._id_category = id_category
        self._description = description

    @staticmethod
    def from_row(row):
        return Category(row[0], row[1])

    def __str__(self):
        return f"Categoria: {self._id_category}, Descripción: {self._description}"

    def __repr__(self):
        return self.__str__()

    @property
    def id_category(self):
        return self._id_category

    @id_category.setter
    def id_category(self, id_category):
        self._id_category = id_category

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description