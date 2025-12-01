
from repository.Conexion import conexion
from domain.Friend import Friend

class FriendRepositoryDB:


    def __init__(self,):
        self.db = conexion(host='localhost', port=3306, user='root', password="", database='book_app')
        self.db.connect()



    def createFriendDB(self, friend):
        query = "INSERT INTO friend (name, phone, mail, adress, rol) VALUES (%s,%s,%s,%s,%s)"
        values = (
            friend.name,
            friend.phone,
            friend.mail,
            friend.adress,
            friend.rol
        )
        self.db.execute_query(query, values)




    def select_friends(self):
        query = "SELECT * FROM friend"
        result = self.db.execute_query(query)
        if result:
            friend_list = []
            for row in result:
                friend = Friend.from_row(row)
                friend_list.append(friend)
            return friend_list

        else:
            print("registros no encontrados")
            return []

    def select_user_by_id(self, id_friend):
        query = "SELECT * FROM friend WHERE id=%s"
        result = self.db.execute_query(query, (id_friend,))
        if result:
            return Friend.from_row(result[0])
        else:
            print("registro no encontrado")
            return []


    def updateFriend(self, friend):
        query = "UPDATE friend SET name=%s, phone=%s,mail=%s, adress=%s  WHERE id =%s"
        values = (friend.name , friend.phone , friend.mail, friend.adress, friend.id)
        self.db.execute_query(query, values)


    def delete_friend_by_id(self, id):
        query = "DELETE FROM friend WHERE id=%s"
        self.db.execute_query(query, [id])






