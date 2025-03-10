from connection import Database


def test_db_connection():
    """Testaa PostgreSQL-yhteyden toimivuus."""
    try:
        Database.initialize()
        conn = Database.get_connection()
        print("✅ Yhteys PostgreSQL:ään toimii!")
        Database.return_connection(conn)
    except Exception as e:
        print(f"❌ Virhe tietokantayhteydessä: {e}")
    finally:
        Database.close_all_connections()


if __name__ == "__main__":
    test_db_connection()
