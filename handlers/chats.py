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
        return jsonify(Chats=result_list)

    def createChat(self, form):
        result_list = []
        if len(form) != 1:
            return jsonify(Error = "Malformed post request"), 400
        else:
            cname = form['cname']
            if cname:
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
                chat4 = {
                    "cid": "4",
                    "cname": cname
                }
                result_list.append(chat1)
                result_list.append(chat2)
                result_list.append(chat3)
                result_list.append(chat4)
                return jsonify(Chats=result_list)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def searchChats(self, args):
        name = args.get('name')
        result_list = []
        if(len(args) == 1) and name:
            chat1 = {
                "cid": "1",
                "cname": name
            }
            result_list.append(chat1)
        else:
            return jsonify(Error="Malformed query string"), 400
        return jsonify(Chats=result_list)

    def getChatById(self, cid):
        result = {
            "cid": cid,
            "cname": "Fortnite"
        }
        return jsonify(Chat=result)

    def updateChat(self, cid, form):
        if len(form) != 1:
            return jsonify(Error="Malformed update request"), 400
        else:
            cname = form['cname']
            if cname:
                result = {
                    "cid": cid,
                    "cname": cname
                }
                return jsonify(Chat=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400



    def deleteChat(self, cid):
        chatToDelete = {
            "cid": cid,
            "cname": "PUBG"
        }
        return jsonify(DeleteStatus="OK"), 200
