from flask import jsonify


class ChatsHandler:

    def getAllChats(self):
        result_list = []
        chat1 = {
            "cid": "1",
            "cname": "dbProject"
        }
        chat2 = {
            "cid": "2",
            "cname": "friends"
        }
        chat3 = {
            "cid": "3",
            "cname": "family"
        }
        result_list.append(chat1)
        result_list.append(chat2)
        result_list.append(chat3)
        return result_list
