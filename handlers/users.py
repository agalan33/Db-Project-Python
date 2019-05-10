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
        user['upassword'] = row[5]
        user['uphone'] = row[6]
        user['uage'] = row[7]
        return user

    def createUser(self, data):
        print(len(data))
        if len(data) < 7:
            return jsonify(Error="Missing Information")
        firstname = data["first_name"]
        lastname = data["last_name"]
        email = data["email"]
        username = data["username"]
        password = data["password"]
        age = data["age"]
        phone_number = data["phone_number"]
        print(firstname)
        dao = UsersDao()
        uid = dao.createAccount(firstname, lastname, email, username, password, age, phone_number)
        print(uid)
        return jsonify(CreatedUser = uid)
      
    def login(self, data):
        result = {
            'email': data['email'],
            'password': data['password'],
        }
        return jsonify(result)

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

    def updateUser(self, data):
        dao = UsersDao()
        result = dao.updateUser(data['uid'], data['first_name'], data['last_name'], data['email'] , data['username'] , data['password'], data['age'], data['phone_number'])
        return jsonify(Result=result)