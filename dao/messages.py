from config.dbconfig import pg_config
import psycopg2


class MessagesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['host'],
                                                                    pg_config['password'])
        self.conn = psycopg2.connect(connection_url)

    ###########################################
    #             GETS                        #
    ###########################################

    def get_all_messages(self):
        cursor = self.conn.cursor()
        query = "select mid, mimage, mtext, mdate, uid from messages"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_chat_messages(self, cid):
        cursor = self.conn.cursor()
        query = "select mid, mimage, mtext, cid, uid, ufirst_name, ulast_name, mdate " \
                "from messages natural inner join users " \
                "where cid = %s and mimage is not null"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_message(self, mid):
        cursor = self.conn.cursor()
        query = "select mid, mimage, mtext, cid, uid, ufirst_name, ulast_name, mdate " \
                "from messages natural inner join users " \
                "where mid = %s"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_message_replies(self, mid):
        cursor = self.conn.cursor()
        query = "select mid, mimage, mtext, cid, uid, ufirst_name, ulast_name, mdate " \
                "from messages as m inner join replies r on m.mid = r.reply_id natural inner join users " \
                "where original_id = %s"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_posts_per_day(self):
        cursor = self.conn.cursor()
        query = "select date(mdate), count(*) " \
                "from messages " \
                "group by date(mdate)"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    ###########################################
    #             POST                        #
    ###########################################
    def post_message(self, mimage, mtext, uid, cid):
        cursor = self.conn.cursor()
        query = "insert into messages (mimage, mtext, uid, cid) values (%s, %s, %s, %s) returning mid, mdate"
        cursor.execute(query, (mimage, mtext, uid, cid,))
        result = cursor.fetchone()
        self.conn.commit()
        cursor.close()
        return result

    def post_reply(self, mid, mtext, uid, cid):
        cursor = self.conn.cursor()
        query = "insert into messages (mtext, uid, cid) values (%s, %s, %s) returning mid, mdate"
        cursor.execute(query, (mtext, uid, cid,))
        result = cursor.fetchone()
        reply_id = result[0]
        query = "insert into replies (original_id, reply_id) values (%s, %s)"
        cursor.execute(query, (mid, reply_id))
        self.conn.commit()
        cursor.close()
        return result

