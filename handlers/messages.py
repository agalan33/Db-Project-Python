from flask import jsonify
from dao.messages import MessagesDAO
from dao.users import UsersDao
import sys


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
        result['mdate'] = row[7]
        return result

    def build_simple_messege_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['mimage'] = row[1]
        result['mtext'] = row[2]
        result['mdate'] = row[3]
        result['uid'] = row[4]
        return result

    def build_message_dict_attributes(self, mid, mimage, mtext, uid, cid, mdate, ufirst_name, ulast_name):
        result = {}
        result['mid'] = mid
        result['mimage'] = mimage
        result['mtext'] = mtext
        result['mdate'] = mdate
        result['uid'] = uid
        result['cid'] = cid
        result['ufirst_name'] = ufirst_name
        result['ulast_name'] = ulast_name
        return result

    def build_daily_posts_count_dict(self, row):
        result = {}
        result['day'] = row[0]
        result['total'] = row[1]
        return result

    ###########################################
    #             GETS                        #
    ###########################################

    def get_all_messages(self):
        dao = MessagesDAO()
        message_list = dao.get_all_messages()
        result_list = []
        for row in message_list:
            result = self.build_simple_messege_dict(row)
            result_list.append(result)
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
            return jsonify(result)

    def get_replies(self, mid):
        dao = MessagesDAO()
        replies_list = dao.get_message_replies(mid)
        result_list = []
        for row in replies_list:
            result = self.build_message_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def get_posts_per_day(self):
        dao = MessagesDAO()
        count_list = dao.get_posts_per_day()
        result_list = []
        for row in count_list:
            result = self.build_daily_posts_count_dict(row)
            result_list.append(result)
        return jsonify(TotalDailyPosts=result_list)

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

    def createMessage(self, form, uid, cid):
        print(form, file=sys.stderr)
        if len(form) == 2:
            image = form["mimage"]
            text = form["mtext"]
            if image and text:
                dao = MessagesDAO()
                udao = UsersDao()
                row = dao.post_message(image, text, uid, cid)
                mid = row[0]
                mdate = row[1]
                fullname = udao.get_fullname(uid)
                ufirst_name = fullname[0]
                ulast_name = fullname[1]
                new_message = self.build_message_dict_attributes(mid, image, text, uid, cid, mdate,
                                                                 ufirst_name, ulast_name)
                return jsonify(new_message), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
        else:
            return jsonify(Error="Malformed post request"), 400


