from config.dbconfig import pg_config
import psycopg2
from psycopg2 import ProgrammingError

class UsersDao:

    def __init__(self):
        connection_url = "dbname={} user={} host={} password={}".format(
            pg_config['dbname'],
            pg_config['user'],
            pg_config['host'],
            pg_config['password']
        )
        self.conn = psycopg2.connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select uid, username, ufirst_name, ulast_name, uemail, upassword, uphone, uage from users where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def createAccount(self, first_name, last_name, email, username, password, age, phone_number):
        cursor = self.conn.cursor()
        query = "insert into users (username, ufirst_name,ulast_name,uemail,upassword, uphone, uage) " \
                "values (%s,%s,%s,%s,%s, %s, %s) returning uid;"
        cursor.execute(query, (username, first_name, last_name, email, password, phone_number, age,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def updateUser(self, uid, first_name, last_name, email, username, password, age, phone_number):
        cursor = self.conn.cursor()
        query = "UPDATE users SET username = %s, ufirst_name = %s, ulast_name = %s, uemail = %s, upassword = %s, uphone = %s, uage = %s WHERE uid = %s;"
        cursor.execute(query, (username, first_name, last_name, email, password, phone_number, age, uid,))
        self.conn.commit()
        return "Success"


    # Get most active users in the system
    def get_most_active_users(self):
        cursor = self.conn.cursor()
        query = "SELECT date(mdate), username, count(*) FROM messages NATURAL INNER JOIN users GROUP BY date(mdate),username ORDER BY date(mdate);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result