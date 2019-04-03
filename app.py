
from flask import Flask, request, jsonify
from handlers.users import UserHandler
from handlers.contactlist import ContactsHandler
from handlers.reactions import ReactionsHandler
from handlers.dashboard import DashboardHandler
from handlers.chats import ChatsHandler
from handlers.messages import MessagesHandler
from handlers.hashtags import HashtagsHandler
import  json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to DB Project'

###########################################
#             User                        #
###########################################

@app.route('/DbProject/users', methods=['POST'])
def manage_account():
    if request.method == 'POST':
        print('Created New User: ', jsonify(request.form))
        return UserHandler().createUser(request.form)
    else:
        return jsonify(Error="Method Not Allowed"), 405

@app.route('/DbProject/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print('Logged in: ', jsonify(request.form))
        return UserHandler().login(request.form)
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
    elif request.method == 'PUT':
        return UserHandler().updateUser(uid)
    else:
        return jsonify(Error="Method Not Allowed")

###########################################
#             Contact                     #
###########################################

@app.route('/DbProject/users/<int:uid>/contacts', methods=['GET', 'POST'])
def manage_contacts(uid):
    if request.method == 'POST':
        return jsonify(ContactCreated=ContactsHandler().createContact(request.form))
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


@app.route('/DbProject/users/<int:uid>/contacts/<int:cid>', methods=['GET', 'DELETE'])
def manage_contact(uid, cid):
    if request.method == 'GET':
        return ContactsHandler().getContactById(cid)
    if request.method == 'DELETE':
        return ContactsHandler().removeContact(cid)
    else:
        return jsonify(Error="Method Not Allowed"), 405


###########################################
#             Chats                       #
###########################################
@app.route('/DbProject/users/<int:uid>/chats', methods=['GET', 'POST'])
def chats(uid):
    if request.method == 'POST':
        return ChatsHandler().createChat(request.form)
    elif request.method == 'GET':
        if not request.args:
            return ChatsHandler().getAllChats()
        else:
            return ChatsHandler().searchChats(request.args)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DbProject/users/<int:uid>/chats/<int:cid>', methods=['GET', 'PUT', 'DELETE'])
def chatById(uid, cid):
    if request.method == 'GET':
        return ChatsHandler().getChatById(cid)
    elif request.method == 'PUT':
        return ChatsHandler().updateChat(cid, request.form)
    elif request.method == 'DELETE':
        return ChatsHandler().deleteChat(cid)
    else:
        return jsonify(Error="Method not allowed"), 405


###########################################
#             Messages                    #
###########################################

@app.route('/DbProject/users/<int:uid>/chats/<int:cid>/messages', methods=['GET', 'POST'])
def messages(uid, cid):
    if request.method == 'POST':
        return MessagesHandler().createMessage(request.form)
    elif request.method == 'GET':
        return MessagesHandler().getAllMessages()
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DbProject/users/<int:uid>/chats/<int:cid>/messages/<int:mid>', methods=['GET', 'DELETE'])
def messageById(uid, cid, mid):
    if request.method == 'GET':
        return MessagesHandler().getMessageById(mid)
    elif request.method == 'DELETE':
        return MessagesHandler().deleteMessage(mid)
    else:
        return jsonify(Error="Method not allowed"), 405


###########################################
#             Hashtag                     #
###########################################

@app.route('/DbProject/users/<int:uid>/chats/<int:cid>/messages/<int:mid>/hashtags', methods=['GET', 'POST'])
def hashtags(uid, cid, mid):
    if request.method == 'POST':
        return HashtagsHandler().createHashtag(request.form)
    elif request.method == 'GET':
        if not request.args:
            return HashtagsHandler().getHashtags()
        else:
            return HashtagsHandler().searchHashtag(request.args)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DbProject/users/<int:uid>/chats/<int:cid>/messages/<int:mid>/hashtags/<int:hid>', methods=['GET', 'PUT'])
def hashtagById(uid, cid, mid, hid):
    if request.method == 'GET':
        return HashtagsHandler().getHashtagById(hid)
    elif request.method == 'PUT':
        return HashtagsHandler().updateHashtag(hid, request.form)
    else:
        return jsonify(Error="Method not allowed"), 405


###########################################
#             Reactions                   #
###########################################
@app.route('/DbProject/users/<int:uid>/chats/<int:cid>/messages/<int:mid>/reactions', methods=['POST', 'GET'])
def reactions(uid, cid, mid):
    if request.method == 'POST':
        return ReactionsHandler().createReaction(request.form)
    elif request.method == 'GET':
        return ReactionsHandler().getReactions()
    else:
        return jsonify(Error="Method not allowed")

      
@app.route('/DbProject/users/<int:uid>/chats/<int:cid>/messages/<int:mid>/reactions/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def reactionsById(uid, cid, mid, rid):
    if request.method == 'GET':
        return ReactionsHandler().getReactionById(rid)
    elif request.method == 'PUT':
        return ReactionsHandler().updateReactionById(rid, request.form)
    elif request.method == 'DELETE':
        return ReactionsHandler().deleteReactionsById(rid)
    else:
        return jsonify(Error='Method Not Allowed')

###########################################
#            Dashboard                    #
###########################################

@app.route('/DbProject/dashboard', methods=['GET'])
def dashboard():
    if request.method == 'GET':
        return DashboardHandler().getDashboard()
    else:
        return jsonify(Error='Method Not Allowed')


@app.route('/DbProject/dashboard/<int:did>', methods=['PUT'])
def dashboardById(did):
    if request.method == 'PUT':
        return DashboardHandler().updateDashboardById(did, request.form)
    else:
        return jsonify(Error='Method Not Allowed')










if __name__ == '__main__':
    app.run()
