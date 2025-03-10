from owner_repository import OwnerRepository
from animal_repository import AnimalRepository
from lesson_repository import LessonRepository


def test_owner_repository():
    print("🔹 Testataan OwnerRepository...")
    repo = OwnerRepository()
    owner_id = repo.add_owner("Matti Meikäläinen", "0401234567", "matti@example.com")
    print(f"✅ Lisättiin omistaja ID: {owner_id}")

    owner = repo.get_owner(owner_id)
    print(f"🧐 Haettu omistaja: {owner}")

    all_owners = repo.get_all_owners()
    print(f"📜 Kaikki omistajat: {all_owners}")


def test_animal_repository():
    print("\n🔹 Testataan AnimalRepository...")
    repo = AnimalRepository()
    animal_id = repo.add_animal(
        "Bella", "Horse", 2015, owner_id=1, notes="Kiltti hevonen"
    )
    print(f"✅ Lisättiin eläin ID: {animal_id}")

    animal = repo.get_animal(animal_id)
    print(f"🧐 Haettu eläin: {animal}")

    all_animals = repo.get_all_animals()
    print(f"📜 Kaikki eläimet: {all_animals}")


def test_lesson_repository():
    print("\n🔹 Testataan LessonRepository...")
    repo = LessonRepository()
    lesson_id = repo.add_lesson(
        horse_id=1,
        date="2025-03-07",
        duration=60,
        price=30.0,
        student_name="Anna Oppilas",
    )
    print(f"✅ Lisättiin tunti ID: {lesson_id}")

    lesson = repo.get_lesson(lesson_id)
    print(f"🧐 Haettu tunti: {lesson}")

    all_lessons = repo.get_all_lessons()
    print(f"📜 Kaikki tunnit: {all_lessons}")


if __name__ == "__main__":
    test_owner_repository()
    test_animal_repository()
    test_lesson_repository()
