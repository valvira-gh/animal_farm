class UI:

    def __init__(self):
        self.running = True

    def show_main_menu(self):
        print("\n🐾 Animal Logger - Kotitilan eläinkirjanpito 🐾")
        print("1️⃣ Eläimet")
        print("2️⃣ Ratsastustunnit")
        print("0️⃣ Poistu")

    @staticmethod
    def print_line():
        print()
        print("-" * 10)
        print()

    def run(self):
        while self.running:
            self.show_main_menu()
            choice = input("\n⚡ Valitse toiminto: ")

            if choice == "1":
                while True:
                    self.print_line()
                    print("\n🐾 Eläimet 🐾")
                    input()
                    break

            elif choice == "2":
                while True:
                    self.print_line()
                    print("\n🐾 Ratsastustunnit 🐾")
                    input()
                    break
            elif choice == "0":
                print("Suljetaan sovellus...")
                self.running = False
            else:
                print("❌ Virheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    ui = UI()
    ui.run()
