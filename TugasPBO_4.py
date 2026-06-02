#TUGAS PBO TAKE HOME
#AIRIN ZULAIKHA K3524041

# Kelas Abstrak Koleksi (Abstract Class)
from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit):
        self.kode_koleksi = kode_koleksi
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit

    @abstractmethod
    def tampilkan_info(self):
        pass 

# Kelas Buku
class Buku(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, pengarang, penerbit):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.pengarang = pengarang

    def tampilkan_info(self):
        return f"Jenis : Buku\nKode Koleksi : {self.kode_koleksi}\nJudul : {self.judul}\nTahun Terbit : {self.tahun_terbit}\nPengarang : {self.pengarang}\nPenerbit : {self.penerbit}"

# Kelas Majalah
class Majalah(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, edisi):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.edisi = edisi

    def tampilkan_info(self):
        return f"Jenis : Majalah\nKode Koleksi : {self.kode_koleksi}\nJudul : {self.judul}\nTahun Terbit : {self.tahun_terbit}\nPenerbit : {self.penerbit}\nEdisi : {self.edisi}"

# Kelas Jurnal
class Jurnal(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, bidang_studi, impact_factor):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    def tampilkan_info(self):
        return f"Jenis : Jurnal\nKode Koleksi : {self.kode_koleksi}\nJudul : {self.judul}\nTahun Terbit : {self.tahun_terbit}\nPenerbit : {self.penerbit}\nBidang Studi : {self.bidang_studi}\nImpact Factor : {self.impact_factor}"

# Kelas DVD Film Dokumenter
class DvdFilmDokumenter(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, bidang_ilmu, durasi):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.bidang_ilmu = bidang_ilmu
        self.durasi = durasi

    def tampilkan_info(self):
        return f"Jenis : DVD Film Dokumenter\nKode Koleksi : {self.kode_koleksi}\nJudul : {self.judul}\nTahun Terbit : {self.tahun_terbit}\nPenerbit : {self.penerbit}\nBidang Ilmu : {self.bidang_ilmu}\nDurasi : {self.durasi}"

# Kelas Manajer Perpus
class ManajerPerpustakaan:
    def __init__(self):
        self.koleksi = []

    def tambah_koleksi(self, koleksi):
        self.koleksi.append(koleksi)
        print("Tambah Koleksi Sukses! Tekan [ENTER] untuk kembali ke menu.")

    def hapus_koleksi(self, kode_koleksi):
        for koleksi in self.koleksi:
            if koleksi.kode_koleksi == kode_koleksi:
                self.koleksi.remove(koleksi)
                print("Hapus Koleksi Sukses! Tekan [ENTER] untuk kembali ke menu.")
                return
        print("Koleksi tidak ditemukan.")

    def tampilkan_koleksi(self):
        if not self.koleksi:
            print("Tidak ada koleksi untuk ditampilkan.")
        for i, koleksi in enumerate(self.koleksi, 1):
            print(f"\nKoleksi {i}:")
            print(koleksi.tampilkan_info())

# Fungsi untuk menampilkan menu dan mengelola interaksi
def menu():
    manajer = ManajerPerpustakaan()
    
    while True:
        print("\nMENU PROGRAM")
        print("1. Tambah data koleksi")
        print("2. Hapus data koleksi")
        print("3. Tampil semua data koleksi")
        print("4. Keluar")
        
        pilihan = input("Nomor yang dipilih: ")
        
        if pilihan == "1":
            print("\nJENIS KOLEKSI YANG AKAN DITAMBAH")
            print("1. Buku")
            print("2. Majalah")
            print("3. Jurnal")
            print("4. DVD Film Dokumenter")
            
            jenis = input("Nomor yang dipilih: ")
            if jenis == "1":
                kode = input("Masukkan Kode Koleksi: ")
                judul = input("Masukkan Judul: ")
                tahun = input("Masukkan Tahun Terbit: ")
                pengarang = input("Masukkan Pengarang: ")
                penerbit = input("Masukkan Penerbit: ")
                buku = Buku(kode, judul, tahun, pengarang, penerbit)
                manajer.tambah_koleksi(buku)
                print("Tambah Buku Sukses! Tekan [ENTER] untuk kembali ke menu.")
            elif jenis == "2":
                kode = input("Masukkan Kode Koleksi: ")
                judul = input("Masukkan Judul: ")
                tahun = input("Masukkan Tahun Terbit: ")
                penerbit = input("Masukkan Penerbit: ")
                edisi = input("Masukkan Edisi: ")
                majalah = Majalah(kode, judul, tahun, penerbit, edisi)
                manajer.tambah_koleksi(majalah)
                print("Tambah Majalah Sukses! Tekan [ENTER] untuk kembali ke menu.")
            elif jenis == "3":
                kode = input("Masukkan Kode Koleksi: ")
                judul = input("Masukkan Judul: ")
                tahun = input("Masukkan Tahun Terbit: ")
                penerbit = input("Masukkan Penerbit: ")
                bidang_studi = input("Masukkan Bidang Studi: ")
                impact_factor = input("Masukkan Impact Factor: ")
                jurnal = Jurnal(kode, judul, tahun, penerbit, bidang_studi, impact_factor)
                manajer.tambah_koleksi(jurnal)
                print("Tambah Jurnal Sukses! Tekan [ENTER] untuk kembali ke menu.")
            elif jenis == "4":
                kode = input("Masukkan Kode Koleksi: ")
                judul = input("Masukkan Judul: ")
                tahun = input("Masukkan Tahun Terbit: ")
                penerbit = input("Masukkan Penerbit: ")
                bidang_ilmu = input("Masukkan Bidang Ilmu: ")
                durasi = input("Masukkan Durasi: ")
                dvd = DvdFilmDokumenter(kode, judul, tahun, penerbit, bidang_ilmu, durasi)
                manajer.tambah_koleksi(dvd)
                print("Tambah DVD Film Dokumenter Sukses! Tekan [ENTER] untuk kembali ke menu.")
            else:
                print("Pilihan tidak valid.")
            
        elif pilihan == "2":
            kode = input("Masukkan Kode Koleksi yang akan dihapus: ")
            manajer.hapus_koleksi(kode)
            print("Hapus Data Koleksi Sukses! Tekan [ENTER] untuk kembali ke menu.")
            
        elif pilihan == "3":
            manajer.tampilkan_koleksi()
            input("\nTekan [ENTER] untuk kembali ke menu.")
        
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()