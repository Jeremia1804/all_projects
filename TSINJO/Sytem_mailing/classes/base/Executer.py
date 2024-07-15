class Executer:

    @staticmethod
    def query(conn,query):
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        return row
    
    @staticmethod
    def insert(conn,query):
        cursor = conn.cursor()
        cursor.execute(query)