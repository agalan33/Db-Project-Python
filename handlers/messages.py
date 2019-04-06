from flask import jsonify
from dao.messages import MessagesDAO

class MessagesHandler:
    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['mimage'] = row[1]
        result['mtext'] = row[2]
        result['cid'] = row[3]
        result['uid'] = row[4]
        result['ufirst_name'] = row[5]
        result['ulast_name'] = row[6]
        return result

    ###########################################
    #             GETS                        #
    ###########################################

    def getAllMessages(self):
        result_list = []
        msg1 = {
            "mid": "1",
            "mimage": "http://wwww.imgur.com/photos/10",
            "mtext": "Found this photo on reddit XD "
        }
        msg2 = {
            "mid": "2",
            "mimage": "http://wwww.imgur.com/photos/12",
            "mtext": "Found this photo on tumblr XD ",
        }
        msg3 = {
            "mid": "3",
            "mimage": "http://wwww.imgur.com/photos/15",
            "mtext": "Found this photo on imgur :o ",
        }
        result_list.append(msg1)
        result_list.append(msg2)
        result_list.append(msg3)
        return jsonify(result_list)

    def get_chat_messages(self, cid):
        dao = MessagesDAO()
        messages_list = dao.get_chat_messages(cid)
        result_list = []
        for row in messages_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def get_message(self, mid):
        dao = MessagesDAO()
        row = dao.get_message(mid)
        if not row:
            return jsonify(Error="Message not found"), 404
        else:
            result = self.build_message_dict(row)
            return jsonify(Message=result)

    def get_replies(self, mid):
        dao = MessagesDAO()
        replies_list = dao.get_message_replies(mid)
        result_list = []
        for row in replies_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(Replies=result_list)

    ###########################################
    #             OTHER CRUD                  #
    ###########################################

    def deleteMessage(self, mid):
        msgToDelete = {
            "mid": mid,
            "mimage": "http://wwww.imgur.com/photos/10",
            "mtext": "Found this photo on reddit XD ",
        }
        return jsonify(DeleteStatus="OK"), 200

    def createMessage(self, form):
        if len(form) == 2:
            image = form["mimage"]
            text = form["mtext"]
            if image and text:
                msgCreated = {
                    "mid": "4",
                    "mimage": image,
                    "mtext": text
                }
                return jsonify(Messages=msgCreated), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400


