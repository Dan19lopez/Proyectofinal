from repository.Conexion import conexion
from domain.loan import Loan
from domain.Friend import Friend
from domain.object import Object
from domain.Category import Category

class LoanRepository:

    def __init__(self):
        self.db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        self.db.connect()

    def create_loan_db(self, loan):
        query = "INSERT INTO loan (date_loan, date_return, friend_id, object_id, state) VALUES (%s, %s, %s, %s, %s)"
        values = (
            loan.date_loan,
            loan.date_return,
            loan.friend.id if loan.friend else None,
            loan.object.id_object if loan.object else None,
            loan.state
        )
        result = self.db.execute_query(query, values)
        
        # Update object state to 'loaned'
        if loan.object:
            update_query = "UPDATE object SET state='loaned' WHERE id_object=%s"
            self.db.execute_query(update_query, (loan.object.id_object,))
        
        return result

    def select_loans(self):
        query = """
        SELECT l.id_loan, l.date_loan, l.date_return, l.state,
               f.id, f.name, f.phone, f.mail, f.adress, f.rol,
               o.id_object, o.description, o.state as object_state,
               c.id_category, c.description as category_description
        FROM loan l
        LEFT JOIN friend f ON l.friend_id = f.id
        LEFT JOIN object o ON l.object_id = o.id_object
        LEFT JOIN category c ON o.category_id = c.id_category
        """
        result = self.db.execute_query(query)
        if result:
            loan_list = []
            for row in result:
                friend = Friend(row[4], row[5], row[6], row[7], row[8], row[9]) if row[4] else None
                category = Category(row[13], row[14]) if row[13] else None
                obj = Object(row[10], row[11], row[12], category) if row[10] else None
                loan = Loan(row[0], row[1], row[2], friend, obj, row[3])
                loan_list.append(loan)
            return loan_list
        else:
            print("No loans found")
            return []

    def select_loan_by_id(self, id_loan):
        query = """
        SELECT l.id_loan, l.date_loan, l.date_return, l.state,
               f.id, f.name, f.phone, f.mail, f.adress, f.rol,
               o.id_object, o.description, o.state as object_state,
               c.id_category, c.description as category_description
        FROM loan l
        LEFT JOIN friend f ON l.friend_id = f.id
        LEFT JOIN object o ON l.object_id = o.id_object
        LEFT JOIN category c ON o.category_id = c.id_category
        WHERE l.id_loan = %s
        """
        result = self.db.execute_query(query, (id_loan,))
        if result:
            row = result[0]
            friend = Friend(row[4], row[5], row[6], row[7], row[8], row[9]) if row[4] else None
            category = Category(row[13], row[14]) if row[13] else None
            obj = Object(row[10], row[11], row[12], category) if row[10] else None
            return Loan(row[0], row[1], row[2], friend, obj, row[3])
        else:
            print("Loan not found")
            return None

    def update_loan(self, loan):
        query = "UPDATE loan SET date_loan=%s, date_return=%s, friend_id=%s, object_id=%s, state=%s WHERE id_loan=%s"
        values = (
            loan.date_loan,
            loan.date_return,
            loan.friend.id if loan.friend else None,
            loan.object.id_object if loan.object else None,
            loan.state,
            loan.id_loan
        )
        self.db.execute_query(query, values)

    def return_loan(self, id_loan):
        """Mark loan as returned and update object state to available"""
        # First get the loan to find the object
        loan = self.select_loan_by_id(id_loan)
        if loan:
            # Update loan state to 'returned'
            query = "UPDATE loan SET state='returned', date_return=CURRENT_DATE WHERE id_loan=%s"
            self.db.execute_query(query, (id_loan,))
            
            # Update object state to 'available'
            if loan.object:
                update_query = "UPDATE object SET state='available' WHERE id_object=%s"
                self.db.execute_query(update_query, (loan.object.id_object,))
            
            return True
        return False

    def delete_loan_by_id(self, id_loan):
        # First get the loan to find the object
        loan = self.select_loan_by_id(id_loan)
        if loan and loan.object:
            # Update object state to 'available' before deleting loan
            update_query = "UPDATE object SET state='available' WHERE id_object=%s"
            self.db.execute_query(update_query, (loan.object.id_object,))
        
        query = "DELETE FROM loan WHERE id_loan=%s"
        self.db.execute_query(query, (id_loan,))

    def select_active_loans(self):
        """Select loans that are currently active (not returned)"""
        query = """
        SELECT l.id_loan, l.date_loan, l.date_return, l.state,
               f.id, f.name, f.phone, f.mail, f.adress, f.rol,
               o.id_object, o.description, o.state as object_state,
               c.id_category, c.description as category_description
        FROM loan l
        LEFT JOIN friend f ON l.friend_id = f.id
        LEFT JOIN object o ON l.object_id = o.id_object
        LEFT JOIN category c ON o.category_id = c.id_category
        WHERE l.state = 'active'
        """
        result = self.db.execute_query(query)
        if result:
            loan_list = []
            for row in result:
                friend = Friend(row[4], row[5], row[6], row[7], row[8], row[9]) if row[4] else None
                category = Category(row[13], row[14]) if row[13] else None
                obj = Object(row[10], row[11], row[12], category) if row[10] else None
                loan = Loan(row[0], row[1], row[2], friend, obj, row[3])
                loan_list.append(loan)
            return loan_list
        else:
            print("No active loans found")
            return []

    def select_loans_by_friend(self, friend_id):
        """Select all loans for a specific friend"""
        query = """
        SELECT l.id_loan, l.date_loan, l.date_return, l.state,
               f.id, f.name, f.phone, f.mail, f.adress, f.rol,
               o.id_object, o.description, o.state as object_state,
               c.id_category, c.description as category_description
        FROM loan l
        LEFT JOIN friend f ON l.friend_id = f.id
        LEFT JOIN object o ON l.object_id = o.id_object
        LEFT JOIN category c ON o.category_id = c.id_category
        WHERE l.friend_id = %s
        """
        result = self.db.execute_query(query, (friend_id,))
        if result:
            loan_list = []
            for row in result:
                friend = Friend(row[4], row[5], row[6], row[7], row[8], row[9]) if row[4] else None
                category = Category(row[13], row[14]) if row[13] else None
                obj = Object(row[10], row[11], row[12], category) if row[10] else None
                loan = Loan(row[0], row[1], row[2], friend, obj, row[3])
                loan_list.append(loan)
            return loan_list
        else:
            print("No loans found for this friend")
            return []