from flask import jsonify
import json

class ReactionsHandler:
    def createReaction(self, form):
        result = {
            'rid' : 0,
            'like': 0,
            'dislike': 0,
        }
        return jsonify(Reaction = result)

    #Get all reactions (for all messages)
    def getReactions(self):
        result = []
        reaction1 = {
            'rid' : 0,
            'like' : 30,
            'dislike' : 0,
        }

        reaction2 = {
            'rid': 1,
            'like': 572,
            'dislike': 81,
        }

        reaction3 = {
            'rid': 2,
            'like': 5,
            'dislike': 103,
        }

        result.append((reaction1))
        result.append((reaction2))
        result.append((reaction3))

        return jsonify(Reactions = result)



    #Get reaction for a given id
    def getReactionById(seld, rid):
        result = {
            'rid' : rid,
            'like' : 5,
            'dislike' : 103
        }

        return jsonify(Reaction = result)




    def updateReactionById(self, rid, form):
        if len(form) != 2:
            return jsonify(Error="Number of attributes different from 2"), 400
        else:
            ulike = form['like']            #updated like
            udislike = form['dislike']
            if ulike and udislike:
                result = {
                    'rid' : 1,
                    'like' : ulike,
                    'dislike' : udislike
                }

                return jsonify(Update=result), 200
            else:

                return jsonify(Error="Unexpected attributes in update request"), 400




    def deleteReactionsById(self, rid):
        return jsonify(DeleteStatus="OK"), 200