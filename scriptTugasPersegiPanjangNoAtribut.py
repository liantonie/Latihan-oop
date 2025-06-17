class PersegiPanjang:

        def hitungLuas (self, panjang, lebar):
            return panjang * lebar
        
        def hitungKeliling (self, panjang, lebar):
             return 2 * (panjang + lebar)
        
        

perpanjang = PersegiPanjang()

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))


print(f"Hasil hitung Luas Persegi Panjang: {perpanjang.hitungLuas(panjang, lebar)}")
print(f"Hasil hitung Keliing Persegi Panjang: {perpanjang.hitungKeliling(panjang, lebar)}")

