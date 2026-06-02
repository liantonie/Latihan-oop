
class Karyawan:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
    
    def tampilkan_info(self):  
        print(f"Nama: {self.nama}, Jabatan: {self.jabatan}, Gaji: {self.gaji}") 
    
    def kenaikan_gaji(self, persen):
        kenaikanGaji = self.gaji * (persen / 100)
        return self.gaji + kenaikanGaji  

# Pembuatan objek dan pemanggilan method
karyawan1 = Karyawan("Budi", "Manager", 10000000)
karyawan1.tampilkan_info() 

gajiAkhir = karyawan1.kenaikan_gaji(10)
print(f"Gaji setelah kenaikan: {gajiAkhir}")
