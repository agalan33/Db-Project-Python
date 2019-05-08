from flask import jsonify
from dao.chats import ChatsDAO


class ChatsHandler:
    def build_chat_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cname'] = row[1]
        result['uid'] = row[2]
        return result

    def build_chat_attributes(self, cid, cname, uid):
        result = {}
        result['cid'] = cid
        result['cname'] = cname
        result['uid'] = uid
        return result

    ###########################################
    #             GETS                        #
    ###########################################
    def get_all_chats(self):
        dao = ChatsDAO()
        chats_list = dao.get_all_chats()
        result_list = []
        for row in chats_list:
            result = self.build_chat_dict(row)
            result_list.append(result)
        return jsonify(Chats=result_list)

    def get_user_chats(self, uid):
        dao = ChatsDAO()
        chats_list = dao.get_user_chats(uid)
        result_list = []
        for row in chats_list:
            result = self.build_chat_dict(row)
            result_list.append(result)
        return jsonify(result_list)

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

    def get_chat(self, cid, uid):
        dao = ChatsDAO()
        row = dao.get_chat(cid, uid)
        if not row:
            return jsonify(Error="Chat not found"), 404
        else:
            result = self.build_chat_dict(row)
            return jsonify(result)

    ###########################################
    #             OTHER CRUD                  #
    ###########################################
    def createChat(self, form, uid):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            cname = form['cname']
            if cname:
                dao = ChatsDAO()
                cid = dao.create_chat(cname, uid)
                result = self.build_chat_attributes(cid, cname, uid)
                return jsonify(Chats=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

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
            return jsonify(user)

    def get_chat_users(self, cid):
        dao = ChatsDAO()
        users_list = dao.get_chat_users(cid)
        result_list = []
        for row in users_list:
            user = {
                'uid': row[0],
                'ufirst_name': row[1],
                'ulast_name:': row[2]
            }
            result_list.append(user)
        return jsonify(result_list)

