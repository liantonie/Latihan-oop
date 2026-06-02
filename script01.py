class Hero:

    # Method untuk menampilkan informasi hero
    def show_info(self):
        print(f"Hero Name: {self.name}, Weapon: {self.weapon}")

    # Method untuk melakukan aksi
    def attack(self):
        print(f"{self.name} is attacking with {self.weapon}!")

        
    # Konstruktor (__init__) untuk menginisialisasi atribut
    def __init__(self, name, weapon):
        self.name = name      # Atribut name
        self.weapon = weapon    # Atribut weapon

# Membuat objek dari class Hero
hero1 = Hero("Batman", "Batarang")
hero2 = Hero("Spiderman", "Web-shooters")

# Menggunakan method dari objek
hero1.show_info()
hero1.attack()

hero2.show_info()
hero2.attack()
