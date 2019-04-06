from config.dbconfig import pg_config
import psycopg2


class MessagesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['host'],
                                                                    pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    ###########################################
    #             GETS                        #
    ###########################################

    def get_all_messages(self):
        cursor = self.conn.cursor()
        query = "select * from messages"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_chat_messages(self, cid):
        cursor = self.conn.cursor()
        query = "select mid, mimage, mtext, cid, uid, ufirst_name, ulast_name " \
                "from messages natural inner join users " \
                "where cid = %s"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_message(self, mid):
        cursor = self.conn.cursor()
        query = "select mid, mimage, mtext, cid, uid, ufirst_name, ulast_name " \
                "from messages natural inner join users " \
                "where mid = %s"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_message_replies(self, mid):
        cursor = self.conn.cursor()
        query = "select mid, mimage, mtext, cid, uid, ufirst_name, ulast_name " \
                "from messages as m inner join replies r on m.mid = r.reply_id natural inner join users " \
                "where original_id = %s"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result


