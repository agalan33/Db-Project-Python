from flask import jsonify
import json

class UserHandler:

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
        result = {
            'uid': uid,
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'username': 'manu',
            'password': 'colegio',
            'age':'47',
            'phone_number': '787-000-0000'
        }
        return jsonify(Users = result)

    def getAllUsers(self):
        result = []
        user1 = {
            'uid': 1,
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'username': 'manu',
            'password': 'colegio',
            'age': '47',
            'phone_number': '787-000-0000'
        }
        user2 = {
            'uid': 2,
            'first_name': 'Jean',
            'last_name': 'Perez',
            'email': 'jean.perez@upr.edu',
            'username': 'jean',
            'password': 'colegio',
            'age': '18',
            'phone_number': '787-100-0100'
        }
        user3 = {
            'uid': 3,
            'first_name': 'Carlos',
            'last_name': 'Rivera',
            'email': 'carlos.rivera@upr.edu',
            'username': 'crivera',
            'password': 'colegio',
            'age': '47',
            'phone_number': '787-040-0500'
        }
        result.append(user1)
        result.append(user2)
        result.append(user3)
        return jsonify(Users = result)
