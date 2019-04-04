from config.dbconfig import pg_config
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
        query = "select * from chat;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_chat_owner(self, cid):
        cursor = self.conn.cursor()
        query = "select uid, ufirst_name, ulast_name from users natural inner join chat where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        cursor.close()
        return result
