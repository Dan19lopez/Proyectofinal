

class Rol:


    def __init__(self, id_rol, description):
        self._id_rol = id_rol
        self._description = description


    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description