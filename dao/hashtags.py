from config.dbconfig import pg_config
import psycopg2


class HashtagsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['host'],
                                                                    pg_config['password'])
        self.conn = psycopg2.connect(connection_url)

    ###########################################
    #               GETS                      #
    ###########################################


    #Get all hashtags in system
    def get_hashtags(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM hashtags;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    # Get top 10 hashtags and respective position depending on times used
    def get_trending_hashtags(self):
        cursor = self.conn.cursor()
        query = "SELECT htext, ROW_NUMBER () OVER (ORDER BY COUNT(htext) DESC) FROM contains NATURAL INNER JOIN hashtags GROUP BY htext ORDER BY COUNT(htext) DESC FETCH FIRST 10 ROWS ONLY;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        cursor.close()
        return result

    #Get hashtag with id equal to hid
    def get_hashtag_by_id(self, hid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM hashtags WHERE hid = %s;"
        cursor.execute(query, (hid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    # Get times used for hashtag with id equal to hid
    def get_times_used(self, hid):
        cursor = self.conn.cursor()
        query = "SELECT COUNT(hid) FROM contains NATURAL INNER JOIN hashtags WHERE hid = %s;"
        cursor.execute(query, (hid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    # Get hashtags contained in message with id equal to mid
    def get_hashtags_per_message(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT hid, htext FROM contains NATURAL INNER JOIN hashtags WHERE mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    # Get messages that used hashtag with id equal to hid
    def get_messages_with_hashtag(self,hid):
        cursor = self.conn.cursor()
        query = "SELECT mid,mtext FROM contains NATURAL INNER JOIN hashtags NATURAL INNER JOIN messages WHERE hid = %s;"
        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result
