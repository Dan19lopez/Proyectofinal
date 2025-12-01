


class User:

    def __init__(self, id, name, phone, mail):
        self._id = id
        self._name = name
        self._phone = phone
        self._mail = mail



    #Getters and Setters

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail




    # Metodos propios





