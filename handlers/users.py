from flask import jsonify
import json

class UserHandler:

    def createUser(data):

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

        return json.dumps(result)

    def searchUsers(uid):
        result = {
            'uid': 1,
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'username': 'manu',
            'password': 'colegio',
            'age':'47',
            'phone_number': '787-000-0000'
        }

        return json.dumps(result)