from flask import jsonify
from dao.reactions import ReactionsDAO
from dao.messages import MessagesDAO
import json


class ReactionsHandler:
    def build_reaction_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rlike'] = row[1]
        result['rdislike'] = row[2]
        result['mid'] = row[3]
        result['uid'] = row[4]
        result['date'] = row[5]
        return result

    def build_reaction_dict_attr(self, rid, rlike, rdislike, mid, uid, rdate):
        result = {}
        result['rid'] = rid
        result['rlike'] = rlike
        result['rdislike'] = rdislike
        result['mid'] = mid
        result['uid'] = uid
        result['date'] = rdate
        return result

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ufirst_name'] = row[1]
        result['ulast_name'] = row[2]
        result['rdate'] = row[3]
        return result

    def createReaction(self, form):
        result = {
            'rid' : 0,
            'like': 0,
            'dislike': 0,
        }
        return jsonify(Reaction = result)


    ###########################################
    #               GETS                      #
    ###########################################

    # Get all reactions in system
    def getReactions(self):
        dao = ReactionsDAO()
        reactions = dao.get_all_reactions()
        result = []
        for row in reactions:
            dict = self.build_reaction_dict(row)
            result.append(dict)
        return jsonify(Reactions=result)

    # Get reaction with id equal to rid
    def getReactionById(self, rid):
        dao = ReactionsDAO()
        reaction = dao.get_reaction_by_id(rid)
        if not reaction:
            return jsonify(Error="Reaction not found"), 404
        else:
            result = self.build_reaction_dict(reaction)
            return jsonify(Reaction=reaction)

    # Get number of likes for message with message id equal to mid
    def get_number_of_likes(self, mid):
        dao = ReactionsDAO()
        message_dao = MessagesDAO()
        message = message_dao.get_message(mid)
        if not message:
            return jsonify(Error="Message does not exist"), 404
        else:
            message_likes = dao.get_number_of_likes_by_mid(mid)
            return jsonify(message_likes)

    # Get number of likes for message with message id equal to mid
    def get_number_of_dislikes(self, mid):
        dao = ReactionsDAO()
        message_dao = MessagesDAO()
        message = message_dao.get_message(mid)
        if not message:
            return jsonify(Error="Message does not exist"), 404
        else:
            message_dislikes = dao.get_number_of_dislikes_by_mid(mid)
            return jsonify(message_dislikes)

    # Get total number of likes in the system
    def get_total_likes(self):
        dao = ReactionsDAO()
        total_likes = dao.get_total_likes()
        return jsonify(Likes=total_likes)

    # Get total number of dislikes in the system
    def get_total_dislikes(self):
        dao = ReactionsDAO()
        total_dislikes = dao.get_total_dislikes()
        return jsonify(Dislikes=total_dislikes)

    # Get list of users that liked message with id equal to mid
    def get_users_that_liked(self, mid):
        dao = ReactionsDAO()
        users = dao.get_users_that_liked_message(mid)
        result = []
        for user in users:
            dict = self.build_user_dict(user)
            result.append(dict)
        return jsonify(result)

    # Get list of users that disliked message with id equal to mid
    def get_users_that_disliked(self, mid):
        dao = ReactionsDAO()
        users = dao.get_users_that_disliked_message(mid)
        result = []
        for user in users:
            dict = self.build_user_dict(user)
            result.append(dict)
        return jsonify(result)

    def get_user_reaction(self, mid, uid):
        dao = ReactionsDAO()
        row = dao.get_user_reaction(mid, uid)
        if not row:
            return jsonify(False)
        else:
            reaction = self.build_reaction_dict(row)
            return jsonify(reaction)

    ###########################################
    #                CRUD                     #
    ###########################################
    def insert_reaction(self, form, uid, mid):
        if len(form) != 2:
            return jsonify(Error="Number of attributes different from 2"), 400
        else:
            rlike = form['rlike']
            rdislike = form['rdislike']
            if rlike and rdislike:
                dao = ReactionsDAO()
                row = dao.insert_reaction(rlike, rdislike, mid, uid)
                rid = row[0]
                rdate = row[1]
                result = self.build_reaction_dict_attr(rid, rlike, rdislike, mid, uid, rdate)
                return jsonify(result)
            else:
                return jsonify(Error="Malformed post request"), 404

    def updateReactionById(self, rid, form):
        if len(form) != 2:
            return jsonify(Error="Number of attributes different from 2"), 400
        else:
            rlike = form['rlike']
            rdislike = form['rdislike']
            if rlike and rdislike:
                dao = ReactionsDAO()
                row = dao.get_reaction_by_id(rid)
                if not row:
                    return jsonify(Error="Reaction not found"), 404
                else:
                    result = dao.update_reaction(rid, rlike, rdislike)
                    return jsonify(Status=result), 201
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteReactionsById(self, rid):
        return jsonify(DeleteStatus="OK"), 200