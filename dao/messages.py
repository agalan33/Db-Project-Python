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
        query = "select date(mdate), count(*) from messages group by date(mdate) order by date(mdate);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result


    def get_posts_per_day_by_user(self, uid):
        cursor = self.conn.cursor()
        query = "select date(mdate), count(*) from messages where uid = %s group by date(mdate) ORDER BY date(mdate);"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def get_replies_per_day(self):
        cursor = self.conn.cursor()
        query = "SELECT date(mdate), COUNT(*) FROM messages AS M INNER JOIN replies AS R ON M.mid = R.reply_id GROUP BY date(mdate) ORDER BY date(mdate);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result


    def get_number_replies_for_post(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT COUNT(*) FROM messages AS M INNER JOIN replies AS R ON M.mid = R.original_id WHERE M.mid = 5;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result