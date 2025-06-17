# Mendefinisikan kelas Kalkulator tanpa konstruktor
class Kalkulator:
    
    def tambah(self, angka1, angka2):
        return angka1 + angka2

    def kurang(self, angka1, angka2):
        return angka1 - angka2

    def kali(self, angka1, angka2):
        return angka1 * angka2

    def bagi(self, angka1, angka2):
        if angka2 != 0:
            return angka1 / angka2
        else:
            return "Error! Pembagian dengan nol tidak diperbolehkan."

# Membuat objek dari kelas Kalkulator
calc = Kalkulator()

# Meminta input dari pengguna
angka1 = float(input("Masukkan bilangan pertama: "))
angka2 = float(input("Masukkan bilangan kedua: "))

# Menampilkan hasil perhitungan
print(f"Hasil Penjumlahan: {calc.tambah(angka1, angka2)}")
print(f"Hasil Pengurangan: {calc.kurang(angka1, angka2)}")
print(f"Hasil Perkalian: {calc.kali(angka1, angka2)}")
print(f"Hasil Pembagian: {calc.bagi(angka1, angka2)}")
