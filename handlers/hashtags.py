from flask import jsonify
from dao.messages import MessagesDAO
import re


class HashtagsHandler:
    @staticmethod
    def get_mtext_hashtags(mtext):
        return re.findall(r"#(\w+)", mtext)

    def getHashtags(self):
        result_list = []
        hash1 = {
            "hid": "1",
            "htext": "trending",
            "htimes_used": "20"
        }
        hash2 = {
            "hid": "2",
            "htext": "lol",
            "htimes_used": "2"
        }
        hash3 = {
            "hid": "3",
            "htext": "funny",
            "htimes_used": "10"
        }
        result_list.append(hash1)
        result_list.append(hash2)
        result_list.append(hash3)
        return jsonify(Hashtags=result_list)

    def searchHashtag(self, args):
        text = args.get('htext')
        result_list = []
        if len(args) == 1 and text:
            result = {
                "hid": "3",
                "htext": text,
                "htimes_used": "10"
            }
            result_list.append(result)
        else:
            return jsonify(Error="Malformed query string"), 400
        return jsonify(Hashtag=result_list)

    def getHashtagById(self, hid):
        result = {
            "hid": hid,
            "htext": "lol",
            "htimes_used": "10"
        }
        return jsonify(Hashtag=result)

    def createHashtag(self, form):
        text = form['htext']
        times_used = form['htimes_used']
        if len(form) == 2:
            if text and times_used:
                result = {
                    "hid": "4",
                    "htext": text,
                    "htimes_used": times_used
                }
                return jsonify(Hashtag=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
        else:
            return jsonify(Error="Malformed update request"), 400


    def updateHashtag(self, hid, form):
        text = form['htext']
        times_used = form['htimes_used']
        if len(form) == 2:
            if text and times_used:
                result = {
                    "hid": hid,
                    "htext": text,
                    "htimes_used": times_used
                }
                return jsonify(Hashtag=result), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
        else:
            return jsonify(Error="Malformed update request"), 400

    def get_message_hashtags(self, mid):
        message_dao = MessagesDAO()
        row = message_dao.get_message(mid)
        if not row:
            return jsonify(Error="Message not found")
        else:
            mtext = row[2]
            result_list = self.get_mtext_hashtags(mtext)
            return jsonify(Hashtags=result_list)


