

class FriendRepository:

    def __init__(self):
        self.friends = {}




    def createFriendDict(self, id_friend ,friend):
        self.friends.update({id_friend:friend})


    def printFriend(self):
        print(self.friends)

    def updateFriendDict(self, id_friend ,friend):
        self.friends.update({id_friend:friend})

    def removeFriendDict(self, id_friend):
        self.friends.pop(id_friend)
