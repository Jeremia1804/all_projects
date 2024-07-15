import psycopg2
class MyConnection:

    @staticmethod
    def connect():
        try:
            conn = psycopg2.connect(
                host="localhost",
                port="5432", 
                dbname="map", 
                user="jeremia", 
                password="jeremia",
            )
            return conn
        except(Exception,psycopg2.Error) as error:
            print("ERREUR", error)
