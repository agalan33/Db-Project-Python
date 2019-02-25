from flask import jsonify

class MessagesHandler:

    def getAllMessages(self):
        result_list = []
        msg1 = {
            "mid": "1",
            "mimage": "http://wwww.imgur.com/photos/10",
            "mtext": {
                "mbody": "Found this photo on reddit XD ",
                "mhashtag": "#funny"
            }
        }
        msg2 = {
            "mid": "2",
            "mimage": "http://wwww.imgur.com/photos/12",
            "mtext": {
                "mbody": "Found this photo on tumblr XD ",
                "mhashtag": "#LOL"
            }
        }
        msg3 = {
            "mid": "3",
            "mimage": "http://wwww.imgur.com/photos/15",
            "mtext": {
                "mbody": "Found this photo on imgur :o ",
                "mhashtag": "#notsofunny"
            }
        }
        result_list.append(msg1)
        result_list.append(msg2)
        result_list.append(msg3)
        return jsonify(Chats=result_list)

    def getMessageById(self, mid):
        result ={
            "mid": mid,
            "mimage": "http://wwww.imgur.com/photos/10",
            "mtext": {
                "mbody": "Found this photo on reddit XD ",
                "mhashtag": "#funny"
            }
        }
        return jsonify(Message=result)

    def getMessagesByHashtag(self, args):
        mhashtag = args.get('hashtag')
        result_list = []
        if len(args) == 1 and mhashtag:
            msg1 = {
                "mimage": "http://wwww.imgur.com/photos/10",
                "mtext": {
                    "mbody": "Found this photo on reddit XD ",
                    "mhashtag": mhashtag
                }
            }
            msg2 = {
                "mid": "2",
                "mimage": "http://wwww.imgur.com/photos/12",
                "mtext": {
                    "mbody": "Found this photo on tumblr XD ",
                    "mhashtag": mhashtag
                }
            }
            result_list.append(msg1)
            result_list.append(msg2)
        else:
            return jsonify(Error="Malformed query string"), 400
        return jsonify(Chats=result_list)

    def deleteMessage(self, mid):
        msgToDelete = {
            "mid": mid,
            "mimage": "http://wwww.imgur.com/photos/10",
            "mtext": {
                "mbody": "Found this photo on reddit XD ",
                "mhashtag": "#funny"
            }
        }
        return jsonify(DeleteStatus="OK"), 200

    def createMessage(self, form):
        result_list = []
        if len(form) == 3:
            image = form["mimage"]
            #mbody and mhashtag nested in mtext
            #could not get that to work postman
            body = form["mbody"]
            hashtag = form["mhashtag"]
            if image and body and hashtag:
                msg1 = {
                    "mid": "1",
                    "mimage": "http://wwww.imgur.com/photos/10",
                    "mtext": {
                        "mbody": "Found this photo on reddit XD ",
                        "mhashtag": "#funny"
                    }
                }
                msg2 = {
                    "mid": "2",
                    "mimage": "http://wwww.imgur.com/photos/12",
                    "mtext": {
                        "mbody": "Found this photo on tumblr XD ",
                        "mhashtag": "#LOL"
                    }
                }
                msg3 = {
                    "mid": "3",
                    "mimage": "http://wwww.imgur.com/photos/15",
                    "mtext": {
                        "mbody": "Found this photo on imgur :o ",
                        "mhashtag": "#notsofunny"
                    }
                }
                msgCreated = {
                    "mid": "4",
                    "mimage": image,
                    "mtext": {
                        "mbody": body,
                        "mhashtag": hashtag
                    }
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


