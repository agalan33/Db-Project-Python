import json
from flask import jsonify
from dao.contactlist import ContactsDao

class ContactsHandler:

    def map_to_Contact(self, row):
        contact = {}
        contact['contactid'] = row[0]
        contact['username'] = row[1]
        contact['ufirst_name'] = row[2]
        contact['ulast_name'] = row[3]
        contact['uemail'] = row[4]
        contact['uphone'] = row[5]
        contact['uage'] = row[6]
        return contact

    def getContactByFirstName(self, uid, name):
        dao = ContactsDao()
        result = dao.getContactByFirst_Name(uid, name)
        result = self.map_to_Contact(result)
        return jsonify(result)
      
    def getContactByLastName(self, uid, name):
        dao = ContactsDao()
        result = dao.getContactByLast_Name(uid, name)
        result = self.map_to_Contact(result)
        return jsonify(result)

    def getContactFromUserById(self, uid, cid):
        dao = ContactsDao()
        result = dao.getContactFromUserByID(uid, cid)
        result = self.map_to_Contact(result)
        return jsonify(result)

    def createContact(self, data):
        ownerid = data['ownerid']
        contactid = data['contactid']
        print(ownerid)
        print(contactid)
        dao = ContactsDao()
        cid = dao.createContact(ownerid, contactid)
        return jsonify(Contactid=cid)

    def getAllContacts(self):
        dao = ContactsDao()
        result = dao.getAllContacts()
        mapped_result = []
        for row in result:
            mapped_result.append(self.map_to_Contact(row))
        return jsonify(mapped_result)


    def getAllContactsFromUser(self, uid):
        dao = ContactsDao()
        result = dao.getAllContactsfromUser(uid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.map_to_Contact(r))
        return jsonify(mapped_result)


    def removeContact(self, data):
        ownerid = data['ownerid']
        contactid = data['contactid']
        dao = ContactsDao()
        result = dao.removeContact(ownerid, contactid)
        return jsonify(Deleted=result)

