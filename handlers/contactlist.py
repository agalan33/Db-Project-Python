import json
from flask import jsonify

class ContactsHandler:

    def getContactByFirstName(self, name):
        result = {
            'cid': 1,
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'phone_number': '787-000-0000'
        }
        return json.dumps(result)
      
    def getContactByLastName(self, name):
        result = {
            'cid': 1,
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'phone_number': '787-000-0000'
        }
        return json.dumps(result)

    def getContactById(self, cid):
        result = {
            'cid': cid,
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'phone_number': '787-000-0000'
        }
        return json.dumps(result)

    def createContact(self, data):
        result = {}
        if 'phone_number' not in data:
            result['phone_number'] = ''
        else:
            result['phone_number'] = data['phone_number']
        if 'email' not in data:
            result['email'] = ''
        else:
            result['email'] = data['email']
        result['cid'] = 1
        result['first_name'] = data['first_name']
        result['last_name'] = data['last_name']

        return json.dumps(result)

    def getAllContacts(self):
        result = []
        contact1 = {
            'cid': 1,
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'phone_number': '787-000-0000'
        }
        contact2 = {
            'cid': 2,
            'first_name': 'Jean',
            'last_name': 'Perez',
            'email': 'jean.perez@upr.edu',
            'phone_number': '787-100-0100'
        }
        contact3 = {
            'cid': 3,
            'first_name': 'Carlos',
            'last_name': 'Rivera',
            'email': 'carlos.rivera@upr.edu',
            'phone_number': '787-040-0500'
        }
        result.append(contact1)
        result.append(contact2)
        result.append(contact3)
        return jsonify(result)

    def removeContact(self, cid):
        contact1 = {
            'cid': cid,
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'phone_number': '787-000-0000'
        }

        return json.dumps(contact1)
