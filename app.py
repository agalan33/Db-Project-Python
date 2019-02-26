from flask import Flask, request,jsonify
from handlers.users import UserHandler
from handlers.contactlist import ContactsHandler
from handlers.chats import ChatsHandler
from handlers.messages import MessagesHandler
from handlers.hashtags import HashtagsHandler
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


@app.route('/DbProject/chats', methods=['GET', 'POST'])
def chats():
    if request.method == 'POST':
        return ChatsHandler().createChat(request.form)
    elif request.method == 'GET':
        if not request.args:
            return ChatsHandler().getAllChats()
        else:
            return ChatsHandler().searchChats(request.args)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DbProject/chats/<int:cid>', methods=['GET', 'PUT', 'DELETE'])
def chatById(cid):
    if request.method == 'GET':
        return ChatsHandler().getChatById(cid)
    elif request.method == 'PUT':
        return ChatsHandler().updateChat(cid, request.form)
    elif request.method == 'DELETE':
        return ChatsHandler().deleteChat(cid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DbProject/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        return MessagesHandler().createMessage(request.form)
    elif request.method == 'GET':
        return MessagesHandler().getAllMessages()
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DbProject/messages/<int:mid>', methods=['GET', 'DELETE'])
def messageById(mid):
    if request.method == 'GET':
        return MessagesHandler().getMessageById(mid)
    elif request.method == 'DELETE':
        return MessagesHandler().deleteMessage(mid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DbProject/hashtags', methods=['GET', 'POST'])
def hashtags():
    if request.method == 'POST':
        return HashtagsHandler().createHashtag(request.form)
    elif request.method == 'GET':
        if not request.args:
            return HashtagsHandler().getHashtags()
        else:
            return HashtagsHandler().searchHashtag(request.args)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DbProject/hashtags/<int:hid>', methods=['GET', 'PUT'])
def hashtagById(hid):
    if request.method == 'GET':
        return HashtagsHandler().getHashtagById(hid)
    elif request.method == 'PUT':
        return HashtagsHandler().updateHashtag(hid, request.form)
    else:
        return jsonify(Error="Method not allowed"), 405


if __name__ == '__main__':
    app.run()
