from db.db import Database


class HorseRepository:
    def __init__(self):
        self.db = Database()

    def add_horse(self, animal_id, breed, color, training_level, is_available):
        sql = """INSERT INTO horses (animal_id, breed, color, training_level, is_available)
        VALUES (%s, %s, %s, %s, %s) RETURNING id"""
        return self.db.query(
            sql, (animal_id, breed, color, training_level, is_available)
        )[0]["id"]

    def get_horse(self, horse_id):
        sql = "SELECT * FROM horses WHERE id = %s"
        result = self.db.query(sql, (horse_id,))
        return result[0] if result else None

    def get_all_horses(self):
        return self.db.query("SELECT * FROM horses")
