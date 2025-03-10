from db.db import Database


class LessonRepository:
    def __init__(self):
        self.db = Database()

    def add_lesson(self, horse_id, date, duration, price, student_name):
        sql = """INSERT INTO lessons (horse_id, date, duration, price, student_name) 
        VALUES (%s, %s, %s, %s, %s) RETURNING id"""
        return self.db.query(sql, (horse_id, date, duration, price, student_name))[0][
            "id"
        ]

    def get_lesson(self, lesson_id):
        sql = "SELECT * FROM lessons WHERE id = %s"
        result = self.db.query(sql, (lesson_id,))
        return result[0] if result else None

    def get_all_lessons(self):
        return self.db.query("SELECT * FROM lessons")

    def delete_lesson(self, lesson_id):
        self.db.execute("DELETE FROM lessons WHERE id = %s", (lesson_id,))
