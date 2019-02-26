
from flask import Flask, request, jsonify
from handlers.users import UserHandler
from handlers.contactlist import ContactsHandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to DB Project'

@app.route('/DbProject/create_account', methods=['POST'])
def manage_account():
    if request.method == 'POST':
        print('Created New User: ', jsonify(request.args))
        return jsonify(CreatedUser=UserHandler().createUser(request.args))
    else:
        return jsonify(Error="Method Not Allowed"), 405

@app.route('/DbProject/users', methods=['GET'])
def manage_users():
    if request.method == 'GET':
        if not request.args:
            return UserHandler().getAllUsers()
        else:
            return UserHandler().getUsersById(request.args)

@app.route('/DbProject/users/<int:uid>', methods=['GET'])
def manage_user(uid):
    if request.method == 'GET':
        return UserHandler().getUsersById(uid)
    return jsonify(Error="Method Not Allowed")

@app.route('/DbProject/contacts', methods=['GET', 'POST'])
def manage_contacts():
    if request.method == 'POST':
        return jsonify(ContactCreated=ContactsHandler().createContact(request.args))
    elif request.method == 'GET':
        if not request.args:
            return ContactsHandler().getAllContacts()
        else:
            req = request.args
            if 'first_name' not in req:
                return ContactsHandler().getContactByLastName(req)

            return ContactsHandler().getContactByFirstName(req)
    else:
        return jsonify(Error="Method Not Allowed"), 405


@app.route('/DbProject/contacts/<int:cid>', methods=['GET', 'DELETE'])
def manage_contact(cid):
    if request.method == 'GET':
        return ContactsHandler().getContactById(cid)
    if request.method == 'DELETE':
        return jsonify(Deleted=ContactsHandler().removeContact(cid))
    else:
        return jsonify(Error="Method Not Allowed"), 405


if __name__ == '__main__':
    app.run()
