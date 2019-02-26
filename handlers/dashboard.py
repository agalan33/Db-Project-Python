from flask import jsonify
import json

class DashboardHandler:
    def getDashboard(self):
        result = {
            'did' : 0,
            'date' : '25 feb 19',
            'total_messages' : 80000,
            'total_replies' : 250000,
            'total_likes' : 500000,
            'total_dislikes' : 34000,
            'total_users' : 5000,
            'trending_users' : 'Andy, Adahid',
            'trending_hashtag' : '#apex, #nba'
        }

        return jsonify(Dashboard=result)


    def updateDashboardById(self, did, form):
        if len(form) != 8:
            return jsonify(Error="Number of attributes different from 7"), 400
        else:
            udate = form['date']                # U for updated values
            umessages = form['total_messages']
            ureplies = form['total_replies']
            ulikes = form['total_likes']
            udislikes = form['total_dislikes']
            uusers = form['total_users']
            utrending_users = form['trending_users']
            utrending_hashtags = form['trending_hashtags']

            if udate and umessages and ureplies and ulikes and udislikes and uusers and utrending_users and utrending_hashtags:
                result = {
                    'did': 0,
                    'date': udate,
                    'total_messages': umessages,
                    'total_replies': ureplies,
                    'total_likes': ulikes,
                    'total_dislikes': udislikes,
                    'total_users': uusers,
                    'trending_users': utrending_users,
                    'trending_hashtag': utrending_hashtags
                }
                return jsonify(Update=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400


    def getTrendingHashtags(self):
       result = {
           'trending_hashtags' : '#apex, #nba'
       }




    def postsPerDay(self, date):
        result = {
            'date' : date,
            'postsPerDay' : 10000
        }

        return jsonify(Posts=result)




    def repliesPerDay(self, date):
        result = {
            'date': date,
            'repliesPerDay': 25000
        }

        return jsonify(Replies=result)





    def likesPerDay(self, date):
        result = {
            'date': date,
            'likesPerDay': 57000
        }

        return jsonify(Likes=result)



    def dislikesPerDay(self, date):
        result = {
            'date': date,
            'dislikesPerDay': 700
        }

        return jsonify(Dislikes=result)


    def MostActiveUsersPerDay(self, date):
        result = {
            'date': date,
            'mostActiveUsersPerDay': 500
        }

        return jsonify(Users=result)


    #Posts per day for a given user (given user id)
    def postsPerDay(self, date, uid):
        result = {
            'date': date,
            'uid' : uid,
            'postsPerDay': 15
        }

        return jsonify(Posts=result)


    #Given message id
    def repliesToPhoto(self, mid):
        result = {
            'mid': mid,
            'replies': 24
        }

        return jsonify(Replies=result)



    #Given message id
    def likesToPhoto(self, mid):
        result = {
            'mid': mid,
            'likes': 50
        }

        return jsonify(Likes=result)





    #Given message id
    def dislikesToPhoto(self, mid):
        result = {
            'mid': mid,
            'likes': 8
        }

        return jsonify(Dislikes=result)