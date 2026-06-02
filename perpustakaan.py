from abc import ABC, abstractmethod

# ---------------------------------------------------------------------
# Bagian untuk mendeskripsikan struktur class Data Koleksi dan turunannya
# ---------------------------------------------------------------------
# kelas abstrak menunjukkan struktur Data Koleksi
class Koleksi(ABC):
    # konstruktor atribut: kode, judul, tahun, penerbit
    def __init__(self, kode, judul, tahun, penerbit):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun
        self.penerbit = penerbit

    # abstract method 
    @abstractmethod
    def tampilkan_info(self):
        pass

# class Buku yang merupakan turunan dari Koleksi
class Buku(Koleksi):
    # konstruktor atribut Buku
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        # inisialisasi atribut untuk super class nya
        super().__init__(kode, judul, tahun, penerbit)
        # inisialisasi atribut untuk selainnya
        self.pengarang = pengarang

    # overriding method abstrak milik super class
    def tampilkan_info(self):
        return f"Buku [{self.kode}] - {self.judul} ({self.tahun}), Pengarang: {self.pengarang}, Penerbit: {self.penerbit}"

# class Majalah yang merupakan turunan dari Koleksi
class Majalah(Koleksi):
    # konstruktor atribut Majalah
    def __init__(self, kode, judul, tahun, penerbit, edisi):
         # inisialisasi atribut untuk super class nya
        super().__init__(kode, judul, tahun, penerbit)
        # inisialisasi atribut untuk selainnya
        self.edisi = edisi

     # overriding method abstrak milik super class
    def tampilkan_info(self):
        return f"Majalah [{self.kode}] - {self.judul} ({self.tahun}), Penerbit: {self.penerbit}, Edisi: {self.edisi}"

# class Jurnal yang merupakan turunan dari Koleksi
class Jurnal(Koleksi):
     # konstruktor atribut Jurnal
    def __init__(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor):
        # inisialisasi atribut untuk super class nya
        super().__init__(kode, judul, tahun, penerbit)
        # inisialisasi atribut untuk selainnya
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    # overriding method abstrak milik super class
    def tampilkan_info(self):
        return f"Jurnal [{self.kode}] - {self.judul} ({self.tahun}), Penerbit: {self.penerbit}, Bidang: {self.bidang_studi}, Impact Factor: {self.impact_factor}"

# -----------------------------------------------------------------------------
# Bagian untuk mendeskripsikan class yang mengatur fitur aplikasi Perpustakaan
# -----------------------------------------------------------------------------

class Perpustakaan:
    def __init__(self):
        self.koleksi = []

    def tambah_koleksi(self, item):
        self.koleksi.append(item)
        print("Data koleksi berhasil ditambahkan.")

    def hapus_koleksi(self, kode):
        for item in self.koleksi:
            if item.kode == kode:
                self.koleksi.remove(item)
                print("Data koleksi berhasil dihapus.")
                return
        print("Kode koleksi tidak ditemukan.")

    def tampilkan_semua(self):
        if not self.koleksi:
            print("Tidak ada data koleksi.")
        else:
            print("\nDaftar Koleksi:")
            for item in self.koleksi:
                print(item.tampilkan_info())

    def cari_data(self, kode):
        for item in self.koleksi:
            if item.kode == kode:
                print(item.tampilkan_info())
# ---------------------------------------------------
# Bagian untuk mendeskripsikan flow control program
# ---------------------------------------------------

def main():
    perpus = Perpustakaan()

    while True:
        print("\nMenu Program")
        print("1. Tambah data koleksi")
        print("2. Hapus data koleksi")
        print("3. Tampil semua data koleksi")
        print("4. Cari data koleksi")
        print("5. Keluar")

        pilihan = input("Nomor yang dipilih: ")

        if pilihan == '1':
            print("\nJenis Koleksi yang akan ditambah")
            print("1. Buku")
            print("2. Majalah")
            print("3. Jurnal")
            jenis = input("Pilih jenis koleksi: ")

            kode = input("Kode koleksi: ")
            judul = input("Judul: ")
            tahun = input("Tahun terbit: ")
            penerbit = input("Penerbit: ")

            if jenis == '1':
                pengarang = input("Pengarang: ")
                koleksi_baru = Buku(kode, judul, tahun, pengarang, penerbit)
            elif jenis == '2':
                edisi = input("Edisi: ")
                koleksi_baru = Majalah(kode, judul, tahun, penerbit, edisi)
            elif jenis == '3':
                bidang = input("Bidang studi: ")
                impact = input("Impact factor: ")
                koleksi_baru = Jurnal(kode, judul, tahun, penerbit, bidang, impact)
            else:
                print("Jenis koleksi tidak valid.")
                continue

            perpus.tambah_koleksi(koleksi_baru)

        elif pilihan == '2':
            kode_hapus = input("Masukkan kode koleksi yang akan dihapus: ")
            perpus.hapus_koleksi(kode_hapus)

        elif pilihan == '3':
            perpus.tampilkan_semua()

        elif pilihan == '4':
            kode_cari = input("Masukkan kode koleksi yang akan dicari: ")
            perpus.cari_data(kode_cari)

        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
