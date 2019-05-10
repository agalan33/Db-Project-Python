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

    def build_daily_posts_count_dict(self, row):
        result = {}
        result['date'] = row[0]
        result['count'] = row[1]
        return result

    def build_count_dict(self, row):
        result = {}
        result['count'] = row[0]
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

    def get_replies_per_day(self):
        dao = MessagesDAO()
        count_list = dao.get_replies_per_day()
        result_list = []
        for row in count_list:
            result = self.build_daily_posts_count_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def get_number_replies_for_post(self, mid):
        dao = MessagesDAO()
        total = dao.get_number_replies_for_post(mid)
        result_list = []
        result = self.build_count_dict(total)
        result_list.append(result)
        return jsonify(TotalReplies=result_list)

    def get_posts_per_day(self):
        dao = MessagesDAO()
        count_list = dao.get_posts_per_day()
        result_list = []
        for row in count_list:
            result = self.build_daily_posts_count_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def get_posts_per_day_by_user(self, uid):
        dao = MessagesDAO()
        count_list = dao.get_posts_per_day_by_user(uid)
        result_list = []
        for row in count_list:
            result = self.build_daily_posts_count_dict(row)
            result_list.append(result)
        return jsonify(PostsPerDay=result_list)

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


