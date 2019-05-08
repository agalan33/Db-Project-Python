from config.dbconfig import pg_config
import psycopg2


class ChatsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['host'],
                                                                    pg_config['password'])
        self.conn = psycopg2.connect(connection_url)

    def get_all_chats(self):
        cursor = self.conn.cursor()
        query = "select * from chats;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_user_chats(self, uid):
        cursor = self.conn.cursor()
        query = "select iM.cid, cname, iM.uid from chats as C inner join isMember iM on C.cid = iM.cid " \
                "where iM.uid = %s"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_chat(self, cid, uid):
        cursor = self.conn.cursor()
        query = "select * from chats where cid = (select cid from isMember where cid = %s and uid = %s)"
        cursor.execute(query, (cid, uid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_chat_owner(self, cid):
        cursor = self.conn.cursor()
        query = "select uid, ufirst_name, ulast_name from users natural inner join chats where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_chat_users(self, cid):
        cursor = self.conn.cursor()
        query = "select uid, ufirst_name, ulast_name " \
                "from users natural inner join ismember " \
                "where cid = 1"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def create_chat(self, cname, uid):
        cursor = self.conn.cursor()
        query = "insert into chats(cname, uid) values (%s, %s) returning cid"
        cursor.execute(query, (cname, uid,))
        cid = cursor.fetchone()[0]
        query = "insert into ismember(uid, cid) values (%s, %s)"
        cursor.execute(query, (uid, cid,))
        self.conn.commit()
        return cid
