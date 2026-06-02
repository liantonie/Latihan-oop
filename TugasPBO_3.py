from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode, judul, tahun):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun

    @abstractmethod
    def display_info(self):
        pass

class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, penulis, penerbit):
        super().__init__(kode, judul, tahun)
        self.penulis = penulis
        self.penerbit = penerbit

    def display_info(self):
        return f"Buku: [{self.kode}] {self.judul} ({self.tahun}) oleh {self.penulis}, diterbitkan oleh {self.penerbit}"

class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun)
        self.penerbit = penerbit
        self.edisi = edisi

    def display_info(self):
        return f"Majalah: [{self.kode}] {self.judul} ({self.tahun}), Edisi {self.edisi}, diterbitkan oleh {self.penerbit}"

class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor):
        super().__init__(kode, judul, tahun)
        self.penerbit = penerbit
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    def display_info(self):
        return f"Jurnal: [{self.kode}] {self.judul} ({self.tahun}), Bidang: {self.bidang_studi}, Impact Factor: {self.impact_factor}, diterbitkan oleh {self.penerbit}"

class DVDFilmDokumenter(Koleksi):
    def __init__(self, kode, judul, tahun, jenis, bidang_ilmu, durasi):
        super().__init__(kode, judul, tahun)
        self.jenis = jenis
        self.bidang_ilmu = bidang_ilmu
        self.durasi = durasi

    def display_info(self):
        return f"DVD Dokumenter: [{self.kode}] {self.judul} ({self.tahun}), Jenis: {self.jenis}, Bidang Ilmu: {self.bidang_ilmu}, Durasi: {self.durasi} menit"

koleksi_perpustakaan = []

def kode_koleksi_unik(kode):
    return any(koleksi.kode == kode for koleksi in koleksi_perpustakaan)

def tambah_koleksi():
    while True:
        try:
            print("=" * 50)
            print("JENIS KOLEKSI YANG AKAN DITAMBAH".center(50))
            print("=" * 50)
            print("1. Buku")
            print("2. Majalah")
            print("3. Jurnal")
            print("4. DVD Film Dokumenter")
            print("=" * 50)
            jenis = int(input("\nNomor yang dipilih: "))

            if jenis not in [1, 2, 3, 4]:
                print("⚠ Pilihan tidak valid!")
                continue

            print("=" * 50)
            if jenis == 1:
                print("TAMBAH DATA BUKU".center(50))
            elif jenis == 2:
                print("TAMBAH DATA MAJALAH".center(50))
            elif jenis == 3:
                print("TAMBAH DATA JURNAL".center(50))
            elif jenis == 4:
                print("TAMBAH DATA DVD FILM DOKUMENTER".center(50))
            print("=" * 50)

            kode = input("\nMasukkan Kode Koleksi: ")

            while kode_koleksi_unik(kode):
                print("⚠ Kode koleksi sudah digunakan! Masukkan kode yang berbeda.")
                kode = input("Masukkan Kode Koleksi yang baru: ")

            judul = input("Masukkan Judul: ")
            tahun = input("Masukkan Tahun Terbit: ")

            if jenis == 1:
                penulis = input("Masukkan Pengarang: ")
                penerbit = input("Masukkan Penerbit: ")
                koleksi_perpustakaan.append(Buku(kode, judul, tahun, penulis, penerbit))
                print("=" * 50)
                print("✅ Tambah Buku sukses".center(50))
            elif jenis == 2:
                penerbit = input("Masukkan Penerbit: ")
                edisi = input("Masukkan Edisi: ")
                koleksi_perpustakaan.append(Majalah(kode, judul, tahun, penerbit, edisi))
                print("=" * 50)
                print("✅ Tambah Majalah sukses".center(50))
            elif jenis == 3:
                penerbit = input("Masukkan Penerbit: ")
                bidang_studi = input("Masukkan Bidang Studi: ")
                impact_factor = input("Masukkan Impact Factor: ")
                koleksi_perpustakaan.append(Jurnal(kode, judul, tahun, penerbit, bidang_studi, impact_factor))
                print("=" * 50)
                print("✅ Tambah Jurnal sukses".center(50))
            elif jenis == 4:
                jenis_film = input("Masukkan Jenis: ")
                bidang_ilmu = input("Masukkan Bidang Ilmu: ")
                durasi = input("Masukkan Durasi (menit): ")
                koleksi_perpustakaan.append(DVDFilmDokumenter(kode, judul, tahun, jenis_film, bidang_ilmu, durasi))
                print("=" * 50)
                print("✅ Tambah DVD Film Dokumenter sukses".center(50))

            input("Tekan [ENTER] untuk kembali ke menu program")
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid!")

def hapus_koleksi():
    print("=" * 50)
    print("HAPUS DATA KOLEKSI".center(50))
    print("=" * 50)
    kode = input("\nMasukkan kode koleksi: ")

    for koleksi in koleksi_perpustakaan:
        if koleksi.kode == kode:
            koleksi_perpustakaan.remove(koleksi)
            print("=" * 50)
            print("✅ Hapus data koleksi sukses".center(50))
            input("Tekan [ENTER] untuk kembali ke menu program")
            return

    print("⚠ Kode koleksi tidak ditemukan!")
    input("Tekan [ENTER] untuk kembali ke menu program")

def tampil_koleksi():
    print("=" * 50)
    print("DAFTAR SEMUA KOLEKSI".center(50))
    print("=" * 50)
    
    if not koleksi_perpustakaan:
        print("Tidak ada koleksi di perpustakaan.".center(50))
    else:
        kategori = {
            "📚 BUKU": [k for k in koleksi_perpustakaan if isinstance(k, Buku)],
            "📖 MAJALAH": [k for k in koleksi_perpustakaan if isinstance(k, Majalah)],
            "📄 JURNAL": [k for k in koleksi_perpustakaan if isinstance(k, Jurnal)],
            "🎥 DVD FILM DOKUMENTER": [k for k in koleksi_perpustakaan if isinstance(k, DVDFilmDokumenter)]
        }

        for kategori_nama, daftar in kategori.items():
            if daftar:
                print("\n" + kategori_nama.center(50))
                print("-" * 50)
                for item in daftar:
                    print("   " + item.display_info())

    input("\nTekan [ENTER] untuk kembali ke menu program")

def main():
    while True:
        print("=" * 50)
        print("MENU PROGRAM".center(50))
        print("=" * 50)
        print("1. Tambah data koleksi")
        print("2. Hapus data koleksi")
        print("3. Tampil semua data koleksi")
        print("4. Keluar")
        print("=" * 50)

        try:
            pilihan = int(input("\nNomor yang dipilih: "))

            if pilihan == 1:
                tambah_koleksi()
            elif pilihan == 2:
                hapus_koleksi()
            elif pilihan == 3:
                tampil_koleksi()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan program ini!")
                break
            else:
                print("⚠ Pilihan tidak valid, silakan coba lagi.")
        except ValueError:
            print("⚠ Masukkan angka yang valid!")

main()
