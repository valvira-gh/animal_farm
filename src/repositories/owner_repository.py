from db.connection import Database

Database.initialize()


class OwnerRepository:
    def add_owner(self, name, phone, email):
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                query = """INSERT INTO owners (name, phone, email)
                VALUES (%s, %s, %s) RETURNING id"""
                cur.execute(query, (name, phone, email))
                owner_id = cur.fetchone()[0]
                conn.commit()
                return owner_id
        finally:
            Database.return_connection(conn)

    def get_owner(self, owner_id):
        """Hakee omistajan tiedot ID:n perusteella."""
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                query = "SELECT * FROM owners WHERE ID = %s"
                cur.execute(query, (owner_id,))
                return cur.fetchone()
        finally:
            Database.return_connection(conn)

    def get_all_owners(self):
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                query = "SELECT * FROM owners"
                cur.execute(query)
                return cur.fetchall()
        finally:
            Database.return_connection(conn)

    def delete_owner(self, owner_id):
        conn = Database.get_connection()
        try:
            with conn.cursor() as cur:
                query = "SELECT * FROM owners WHERE id = %s"
                cur.execute(query, (owner_id))
                conn.commit()
        finally:
            Database.return_connection(conn)


if __name__ == "__main__":
    owner = OwnerRepository()
    owner_id = owner.add_owner("Tarmo Testimies", "0401234567", "tare@gmail.com")
    print("Owner id:", owner_id)
