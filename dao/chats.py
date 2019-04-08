from config_db.dbconfig import pg_config
import psycopg2


class ChatsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['host'],
                                                                    pg_config['passwd'])
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
