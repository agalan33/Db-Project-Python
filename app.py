from flask import Flask, request,jsonify
from handlers.users import UserHandler
from handlers.contactlist import ContactsHandler
import  json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Fake Instagram'


@app.route('/DbProject/create_account', methods=['POST'])
def manager_users():
    if request.method == 'POST':
        print('Created New User: ', jsonify(request.args))
        return UserHandler.createUser(request.args)
    else:
        return jsonify(Error="Method Not Allowed"), 405


@app.route('/DbProject/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        return ContactsHandler.createContact(request.args)
    elif request.method == 'GET':
        req = request.args
        if 'first_name' in req:
            return ContactsHandler.getContactByLastName(req)

        return ContactsHandler.getContactByFirstName(req)

    return jsonify(Error="Method Not Allowed"), 405


if __name__ == '__main__':
    app.run()
