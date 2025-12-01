from domain.Category import Category


class Object:


    def __init__(self, id_object, description, state, category):
        self._id_object = id_object
        self._description = description
        self._state = state
        self._category = category

    @staticmethod
    def from_row(row):
        # Assuming row contains: (id_object, description, state, category_id, category_description)
        category = Category(row[3], row[4]) if len(row) > 4 else None
        return Object(row[0], row[1], row[2], category)

    def __str__(self):
        return f"Object(id={self._id_object}, description={self._description}, state={self._state}, category={self._category})"

    def __repr__(self):
        return self.__str__()

    @property
    def id_object(self):
        return self._id_object

    @id_object.setter
    def id_object(self, id_object):
        self._id_object = id_object

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def state(self):
        return self._state


    @state.setter
    def state(self, state):
        self._state = state

    @property
    def category(self):
        return self._category


    @category.setter
    def category(self, category):
        self._category = category