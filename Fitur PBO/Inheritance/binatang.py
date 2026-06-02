# Superclass
class Binatang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def get_info(self):
        return f"{self.nama} usianya {self.umur} tahun"

# Subclass Kambing
class Kambing(Binatang):
    def bersuara(self):
        return f"{self.nama} mengembek"

# Subclass Kucing
class Kucing(Binatang):
    def bersuara(self):
        return f"{self.nama} mengeong"

# Membuat objek
kambing = Kambing("Dolly", 3)
kucing = Kucing("Kitty", 2)

# Menampilkan hasil
print(kambing.bersuara())   # Output: Dolly mengembek
print(kucing.bersuara())    # Output: Kitty mengeong
print(kambing.get_info())   # Output: Dolly usianya 3 tahun
print(kucing.get_info())    # Output: Kitty usianya 2 tahun