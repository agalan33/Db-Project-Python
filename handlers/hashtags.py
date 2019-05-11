from flask import jsonify
from dao.messages import MessagesDAO
from dao.hashtags import HashtagsDAO
import re


class HashtagsHandler:
    @staticmethod
    def get_mtext_hashtags(mtext):
        return re.findall(r"#(\w+)", mtext)

    def build_trending_dict(self, row):
        result = {}
        result['position'] = row[0]
        result['htext'] = row[1]
        result['count'] = row[2]
        return result

    def build_hashtag_dict(self, row):
        result = {}
        result['hid'] = row[0]
        result['htext'] = row[1]
        return result

    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['mtext'] = row[1]
        return result


    ###########################################
    #               GETS                      #
    ###########################################


    # Get all hashtags in system
    def get_hashtags(self):
        dao = HashtagsDAO()
        hashtags = dao.get_hashtags()
        result = []
        for hashtag in hashtags:
            dict = self.build_hashtag_dict(hashtag)
            result.append(dict)
        return jsonify(Hashtags=result)

    # Get top 10 used hashtags with respective positions
    def get_trending(self):
        dao = HashtagsDAO()
        trending = dao.get_trending_hashtags()
        result = []
        for hashtag in trending:
            dict = self.build_trending_dict(hashtag)
            result.append(dict)
        return jsonify(result)

    # Get hashtags contained in message with id equal to mid
    def get_hashtags_for_message(self, mid):
        dao = HashtagsDAO()
        hashtags = dao.get_hashtags_per_message(mid)
        result = []
        for hashtag in hashtags:
            dict = self.build_hashtag_dict(hashtag)
            result.append(dict)
        return jsonify(Hashtag=result)

    # Get hashtag with id equal to hid
    def get_hashtag_by_id(self, hid):
        dao = HashtagsDAO()
        hashtag = dao.get_hashtag_by_id(hid)
        if not hashtag:
            return jsonify(Error="Hashtag not found"), 404
        else:
            result = self.build_hashtag_dict(hashtag)
            return jsonify(Hashtag=result)

    # Get times used for hashtag with id equal to hid
    def get_times_used(self, hid):
        dao = HashtagsDAO()
        times_used = dao.get_times_used(hid)
        return jsonify(Used=times_used)

    # Get messages that used hashtag with id equal to hid
    def get_messages_with_hashtag(self, hid):
        dao = HashtagsDAO()
        messages = dao.get_messages_with_hashtag(hid)
        result = []
        for message in messages:
            dict = self.build_message_dict(message)
            result.append(dict)
        return jsonify(Messages=result)

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




