from config.dbconfig import pg_config
import psycopg2
from psycopg2 import ProgrammingError

class ContactsDao:

    def __init__(self):
        connection_url = "dbname={} user={} host={} password={}".format(
            pg_config['dbname'],
            pg_config['user'],
            pg_config['host'],
            pg_config['password']
        )
        self.conn = psycopg2.connect(connection_url)

    def getAllContacts(self):
        cursor = self.conn.cursor()
        query = "select contactid, username, ufirst_name, ulast_name, uemail, uphone, uage from users join contacts c on users.uid = contactid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllContactsfromUser(self, uid):
        cursor = self.conn.cursor()
        query = "select contactid, username, ufirst_name, ulast_name, uemail, uphone, uage from users join contacts c on users.uid = contactid where ownerid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContactByFirst_Name(self, uid, name):
        cursor = self.conn.cursor()
        query = "select contactid, username, ufirst_name, ulast_name, uemail, uphone, uage from users join contacts c on users.uid = contactid where ownerid = %s and ufirt_name = %s;"
        cursor.execute(query, (uid, name,))
        result = cursor.fetchone()
        return result

    def getContactByLast_Name(self, uid, name):
        cursor = self.conn.cursor()
        query = "select contactid, username, ufirst_name, ulast_name, uemail, uphone, uage from users join contacts c on users.uid = contactid where ownerid = %s and ulast_name = %s;"
        cursor.execute(query, (uid, name,))
        result = cursor.fetchone()
        return result

    def getContactFromUserByID(self, uid, cid):
        cursor = self.conn.cursor()
        query = "select contactid, username, ufirst_name, ulast_name, uemail, uphone, uage from users join contacts c on users.uid = contactid where ownerid = %s and contactid = %s;"
        cursor.execute(query, (uid, cid,))
        result = cursor.fetchone()
        return result

    def createContact(self, ownerid, contactid):
        cursor = self.conn.cursor()
        query = "insert into contacts (ownerid, contactid) " \
                "values (%s,%s) returning contactid;"
        cursor.execute(query, (ownerid, contactid,))
        uid = cursor.fetchone()[0]
        print(uid)
        self.conn.commit()
        return uid

    def removeContact(self, ownerid, contactid):
        cursor = self.conn.cursor()
        query = "delete from contacts where ownerid = %s and contactid = %s;"
        cursor.execute(query, (ownerid, contactid))
        self.conn.commit()
        return "Successful"
