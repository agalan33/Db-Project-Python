from flask import jsonify
from dao.users import UsersDao
import json

class UserHandler:

    def map_to_User(self, row):
        user = {}
        user['uid'] = row[0]
        user['username'] = row[1]
        user['ufirst_name'] = row[2]
        user['ulast_name'] = row[3]
        user['uemail'] = row[4]
        user['uphone'] = row[5]
        user['uage'] = row[6]
        return user

    def createUser(self, data):
        if len(data) < 7:
            return jsonify(Error="Missing Information")
        result = {
            'uid': 1,
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'username': data['username'],
            'password': data['password'],
            'age': data['age'],
            'phone_number': data['phone_number']
        }
        return jsonify(CreatedUser = result)
      
    def login(self, data):
        result = {
            'email': data['email'],
            'password': data['password'],
        }
        return jsonify(LoggedIn = result)

    def updateUser(self,data,uid):
        result = {
            'uid': uid,
            'email': data['email']
        }
        return jsonify(UpdatedUser = result)


    def getUsersById(self, uid):
        dao = UsersDao()
        result = dao.getUserById(uid)
        result = self.map_to_User(result)
        return jsonify(result)

    def getAllUsers(self):
        result = []
        dao = UsersDao()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_User(r))
        return jsonify(mapped_result)
        return jsonify(result)

    def getUserByUsername(self,username):
        dao = UsersDao()
        result = dao.getUserByUsername(username)
        result = self.map_to_User(result)
        return jsonify(result)
