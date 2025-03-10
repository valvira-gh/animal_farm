from psycopg2 import pool
import os


class Database:
    """PostgreSQL-yhteyksien hallinta."""

    _connection_pool = None

    @classmethod
    def initialize(cls):
        """Alustaa yhteyspoolin ympäristömuuttujien perusteella."""
        cls._connection_pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname=os.getenv("DB_NAME", "animalfarmdb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "sh1m4tt4"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
        )

    @classmethod
    def get_connection(cls):
        """Palauttaa yhteyden tietokantaan."""
        if cls._connection_pool is None:
            raise Exception("Tietokantayhteys ei ole alustettu! Kutsu initialize().")
        return cls._connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        """Palauttaa yhteyden takaisin pooliin."""
        cls._connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        """Sulkee kaikki yhteydet."""
        if cls._connection_pool:
            cls._connection_pool.closeall()


if __name__ == "__main__":
    pass
