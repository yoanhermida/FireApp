import sqlite3


class DatabaseClient:

    def __init__(self, db):
        self.db = db

    def connect(self):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        return cursor


class MyData:

    def __init__(self, client):
        self.client = client

    def get_record(self):
        sql = "SELECT * FROM networth"
        self.client.connect().execute(sql)
        return self.client.connect().fetchall()
