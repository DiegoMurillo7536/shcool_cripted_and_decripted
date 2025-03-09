import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DATABASE_NAME")
user = os.getenv("USER_POSTRES_NAME")
password = os.getenv("USER_POSTRES_PASSWORD")


class Connection:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host="localhost",  # O la IP del servidor
            port="5432"  # Puerto por defecto de PostgreSQL
        )

    def execute(self, query, data ):
        cur = self.conn.cursor()
        cur.execute(query, data)
        self.conn.commit()
        cur.close()
    
    def fetchall(self, query, data):
        cur = self.conn.cursor()
        cur.execute(query, data)
        rows = cur.fetchall()
        cur.close()
        print(rows)
        return rows

    def close(self):
        self.conn.close()