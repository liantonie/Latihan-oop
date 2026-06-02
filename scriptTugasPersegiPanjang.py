class PersegiPanjang:
        def __init__(self, panjang, lebar):
            self.panjang = panjang
            self.lebar = lebar
        

        def hitungLuas (self):
            return self.panjang * self.lebar
        
        def hitungKeliling (self):
             return 2 * (self.panjang + self.lebar)
        

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))


perpanjang = PersegiPanjang(panjang, lebar)

print(f"Hasil hitung Luas Persegi Panjang: {perpanjang.hitungLuas()}")
print(f"Hasil hitung Keliing Persegi Panjang: {perpanjang.hitungKeliling()}")

