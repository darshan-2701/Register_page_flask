import psycopg2
from Utility import DbConfig

class PostgresClass:
    def __init__(self):
        self.host_name = DbConfig.host
        self.user_name = DbConfig.user
        self.password = DbConfig.password
        self.port = DbConfig.port
        self.database = DbConfig.database

    def db_connect(self):
        self.conn = psycopg2.connect(host= self.host_name, user = self.user_name, password = self.password,
                                     database=self.database, port = self.port)
        self.cursor = self.conn.cursor()
        return self.conn
    
    def db_disconnect(self):
        if self.cursor is not None:
            self.cursor.close()

        if self.conn is not None:
            self.conn.close()

    def commit_changes(self):
        self.conn.commit()