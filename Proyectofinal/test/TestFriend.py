from domain.Friend import Friend
from service.FriendService import FriendService







friend = Friend(None,None,None,None,None,None)
friendService = FriendService()


show_friend= friendService.select_friend_by_id(70100100)
print(f"amigo{show_friend}")
