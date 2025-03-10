from db.connection import Database


class AnimalRepository:
    """CRUD-operaatiot eläintaululle"""

    def __init__(self):
        self.db = Database()

        def add_animal(
            self, name: str, species: str, birth_year: int, owner_id=None, notes=None
        ):
            sql = """INSERT INTO animals (name, species, birth_year, owner_id, notes)
            VALUES (%s, %s, %s, %s, %s) RETURNING id"""
            return self.db.query(sql, (name, species, birth_year, owner_id, notes))[0][
                "id"
            ]

        def get_all_animals(self):
            return self.db.query("SELECT * FROM animals")

        def delete_animal(self, animal_id):
            self.db.execute("DELETE FROM animals WHERE id = %s", (animal_id,))
