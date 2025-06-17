class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama  
        self.nim = nim
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}")  

class MataKuliah:
    def __init__(self, nama_mk, sks):
        self.nama_mk = nama_mk
        self.sks = sks
    
    def tampilkan_info(self):
        print(f"Mata Kuliah: {self.nama_mk}, SKS: {self.sks}")  

class KRS:
    def __init__(self):
        self.kuliah_diambil = []
    
    def tambah_mata_kuliah(self, mk):  
        self.kuliah_diambil.append(mk)
    
    def tampilkan_krs(self):
        print("Daftar Mata Kuliah yang Diambil:")
        for mk in self.kuliah_diambil:
            print(f"- {mk.nama_mk} ({mk.sks} SKS)")

# Pembuatan objek dan pemanggilan method

# membuat data matakuliah
mk1 = MataKuliah("Pemrograman Berorientasi Objek", 3)
mk2 = MataKuliah("Struktur Data", 4)

# membuat data mahasiswa
mhs = Mahasiswa("Andi", "123456")
mhs.tampilkan_info()

# tambah mata kuliah pada tiap mahasiswa
krs = KRS()
krs.tambah_mata_kuliah(mk1)  
krs.tambah_mata_kuliah(mk2)
krs.tampilkan_krs()
