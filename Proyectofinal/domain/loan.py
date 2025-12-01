
from domain.Friend import Friend
from domain.object import Object


class Loan:
    def __init__(self, id_loan, date_loan, date_return, friend, object, state):
        self._id_loan = id_loan
        self._date_loan = date_loan
        self._date_return = date_return
        self._friend = friend
        self._object = object
        self._state = state

    @staticmethod
    def from_row(row):
        # Assuming row contains loan data with friend and object details
        # This would need to be adjusted based on your actual database JOIN query
        return Loan(row[0], row[1], row[2], row[3], row[4], row[5])

    def __str__(self):
        return f"Loan(id={self._id_loan}, date_loan={self._date_loan}, date_return={self._date_return}, friend={self._friend}, object={self._object}, state={self._state})"

    def __repr__(self):
        return self.__str__()

    @property
    def id_loan(self):
        return self._id_loan

    @id_loan.setter
    def id_loan(self, id_loan):
        self._id_loan = id_loan

    @property
    def date_loan(self):
        return self._date_loan

    @date_loan.setter
    def date_loan(self, date_loan):
        self._date_loan = date_loan

    @property
    def date_return(self):
        return self._date_return

    @date_return.setter
    def date_return(self, date_return):
        self._date_return = date_return

    @property
    def friend(self):
        return self._friend

    @friend.setter
    def friend(self, friend):
        self._friend = friend

    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, object):
        self._object = object

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
