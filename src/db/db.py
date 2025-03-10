import psycopg2
from psycopg2.extras import DictCursor
import os


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        self.conn.autocommit = True  # Muutokset tallennetaan automaattisesti

    def query(self, sql, params=None):
        """Yleinen metodi SELECT-kyselyille"""
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql, params or ())
            return cur.fetchall()

    def execute(self, sql, params=None):
        """Yleinen metodi INSERT, UPDATE, DELETE -kyselyille."""
        with self.conn.cursor() as cur:
            cur.execute(sql, params or ())

    def close(self):
        """Sulkee tietokantayhteyden."""
        self.conn.close()


if __name__ == "__main__":
    pass
