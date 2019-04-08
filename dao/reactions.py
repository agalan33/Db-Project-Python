from config_db.dbconfig import pg_config
import psycopg2


class ReactionsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                                    pg_config['user'],
                                                                    pg_config['host'],
                                                                    pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    ###########################################
    #               GETS                      #
    ###########################################


    # Get all reactions in system
    def get_all_reactions(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reactions where rlike = 1;"
        cursor.execute(query)
        result = []
        for row in cursor:
           result.append(row)
        cursor.close()
        return result

    # Get total likes in system
    def get_total_likes(self):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM reactions where rlike = 1;"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result

    # Get total dislikes in system
    def get_total_dislikes(self):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM reactions where rdislike = 1;"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result

    # Get reaction with given reaction id
    def get_reaction_by_id(self, rid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reactions WHERE rid = %s"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    # Get likes for message with id equal to mid
    def get_number_of_likes_by_mid(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM reactions WHERE (mid = %s AND rlike = 1)"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    # Get dislikes for message with id equal to mid
    def get_number_of_dislikes_by_mid(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM reactions WHERE (mid = %s AND rdislike = 1)"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    # Get list of users that liked message with id equal to mid
    def get_users_that_liked_message(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT uid, ufirst_name, ulast_name, rdate FROM reactions natural inner join users WHERE mid = %s and rlike = 1"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    # Get list of users that disliked message with id equal to mid
    def get_users_that_disliked_message(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT uid, ufirst_name, ulast_name, rdate FROM reactions natural inner join users WHERE mid = %s and rdislike = 1"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

