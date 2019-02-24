import json

class ContactsHandler:

    def getContactByFirstName(name):
        result = {
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'phone_number': '787-000-0000'
        }
        return json.dumps(result)

    def getContactByLastName(name):
        result = {
            'first_name': 'Manuel',
            'last_name': 'Rodriguez',
            'email': 'manuel.rodriguez@upr.edu',
            'phone_number': '787-000-0000'
        }
        return json.dumps(result)

    def createContact(data):
        result = {}
        if 'phone_number' not in data:
            result['phone_number'] = ''
        else:
            result['phone_number'] = data['phone_number']
        if 'email' not in data:
            result['email'] = ''
        else:
            result['email'] = data['email']
        result['uid'] =  1
        result['first_name'] = data['first_name']
        result['last_name'] = data['last_name']

        return json.dumps(result)
