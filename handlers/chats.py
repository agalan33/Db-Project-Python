from flask import jsonify
from dao.chats import ChatsDAO


class ChatsHandler:
    def build_chat_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cname'] = row[1]
        result['uid'] = row[2]
        return result

    def get_all_chats(self):
        dao = ChatsDAO()
        chats_list = dao.get_all_chats()
        result_list = []
        for row in chats_list:
            result = self.build_chat_dict(row)
            result_list.append(result)
        return jsonify(Chats=result_list)

    def createChat(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            cname = form['cname']
            if cname:
                result = {
                    "cid": "4",
                    "cname": cname
                }
                return jsonify(Chats=result), 201
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

    def get_chat_owner(self, cid):
        dao = ChatsDAO()
        row = dao.get_chat_owner(cid)
        if not row:
            return jsonify(Error="User not found"), 404
        else:
            user = {
                'uid': row[0],
                'ufirst_name': row[1],
                'ulast_name:': row[2]
            }
            return jsonify(User=user)

