from domain.User import User


class Friend (User):

    # Constructor de la clase

    def __init__(self, id, name, phone, mail, adress, rol):
        super().__init__(id, name, phone, mail)
        self._adress = adress
        self._rol = rol

    @staticmethod
    def from_row(row):
        return Friend(row[0], row[1], row[2], row[3], row[4], row[5])

    def __str__(self):
        return f"Friend(id={self.id}, nombre={self.name}, apellido={self.phone}, edad={self.mail}, ciudad={self.adress}, estado={self.rol})"


    def __repr__(self):
        return self.__str__()



    #Getters and Setters

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, adress):
        self._adress = adress

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol



    # Metodos propios






