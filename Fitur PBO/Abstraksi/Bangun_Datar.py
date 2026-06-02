from abc import ABC, abstractmethod
 
class BangunDatar(ABC):
    @abstractmethod
    def hitungLuas(self):   
        pass
    @abstractmethod
    def hitungKeliling(self):
        pass
 
class PersegiPanjang(BangunDatar):
    panjang = 0
    lebar = 0
    # implementasi hitungLuas()
    def hitungLuas(self):
        return self.panjang * self.lebar
    # implementasi hitungKeliling()
    def hitungKeliling(self):
        return 2*(self.panjang + self.lebar)
 
class Lingkaran(BangunDatar):
    jejari = 0
    # implementasi hitungLuas()
    def hitungLuas(self):
        return 3.14 * self.jejari * self.jejari
    # implementasi hitungKeliling()
    def hitungKeliling(self):
        return 2 * 3.14 * self.jejari
    
class Segitiga(BangunDatar):
    alas = 0
    tinggi = 0
    def hitungLuas(self):
        return 0.5 * self.alas * self.tinggi
    def hitungKeliling(self):
        return super().hitungKeliling()
    


# menghitung luas dan keliling persegi panjang dengan p = 10 dan l = 5
a = PersegiPanjang()
a.panjang = 10
a.lebar = 5
print("Luas persegi panjang:", a.hitungLuas())
print("Keliling persegi panjang:", a.hitungKeliling())
 
# menghitung luas dan keliling lingkaran berjejari 10
b = Lingkaran()
b.jejari = 10
print("Luas lingkaran:", b.hitungLuas())
print("Keliling lingkaran:", b.hitungKeliling())

c = Segitiga()
c.tinggi = 10
c.alas = 5
print("Luas segitiga:", c.hitungLuas())
print("Keliling segitiga:", c.hitungKeliling())