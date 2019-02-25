from flask import jsonify

class MessagesHandler:

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
        return jsonify(Chats=result_list)

    def getMessageById(self, mid):
        result ={
            "mid": mid,
            "mimage": "http://wwww.imgur.com/photos/10",
            "mtext": "Found this photo on reddit XD "
        }
        return jsonify(Message=result)


    def deleteMessage(self, mid):
        msgToDelete = {
            "mid": mid,
            "mimage": "http://wwww.imgur.com/photos/10",
            "mtext": "Found this photo on reddit XD ",
        }
        return jsonify(DeleteStatus="OK"), 200

    def createMessage(self, form):
        result_list = []
        if len(form) == 2:
            image = form["mimage"]
            text = form["mtext"]
            if image and text:
                msg1 = {
                    "mid": "1",
                    "mimage": "http://wwww.imgur.com/photos/10",
                    "mtext": "Found this photo on reddit XD ",
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
                msgCreated = {
                    "mid": "4",
                    "mimage": image,
                    "mtext": text
                }
                result_list.append(msg1)
                result_list.append(msg2)
                result_list.append(msg3)
                result_list.append(msgCreated)
                return jsonify(Chats=result_list)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400


