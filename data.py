from datetime import datetime
import sqlite3


class DatabaseClient:

    conn = sqlite3.connect("fireapp.db")

    cursor = conn.cursor()


class MyData:

    # insert record
    net_worth_document = {
        'age': 35,
        'date': datetime.now(),
        'projected': 1.00,
        'actual': 2.00
    }
