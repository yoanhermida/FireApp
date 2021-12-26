import sqlite3


class DatabaseClient:

    def __init__(self, db):
        self.db = db

    def connect(self):
        conn = sqlite3.connect(self.db)
        curs = conn.cursor()
        return curs

    def get_record(self):
        sql = "SELECT * FROM networth"
        q = self.connect().execute(sql)
        return q.fetchall()
