# Mendefinisikan kelas Kalkulator
class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def tambah(self):
        return self.angka1 + self.angka2

    def kurang(self):
        return self.angka1 - self.angka2

    def kali(self):
        return self.angka1 * self.angka2

    def bagi(self):
        if self.angka2 != 0:
            return self.angka1 / self.angka2
        else:
            return "Error! Pembagian dengan nol tidak diperbolehkan."

# Meminta input dari pengguna
angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))

# Membuat objek dari kelas Kalkulator
calc = Kalkulator(angka1, angka2)

# Menampilkan hasil perhitungan
print(f"Hasil Penjumlahan: {calc.tambah()}")
print(f"Hasil Pengurangan: {calc.kurang()}")
print(f"Hasil Perkalian: {calc.kali()}")
print(f"Hasil Pembagian: {calc.bagi()}")
