from abc import ABC, abstractmethod 
 
class Koleksi(ABC): 
    def __init__(self, kode, judul, tahun): 
        self.kode = kode 
        self.judul = judul 
        self.tahun = tahun 
 
    @abstractmethod 
    def display_info(self): 
        pass 
 
    def __str__(self): 
        return self.display_info() 
 
class Buku(Koleksi): 
    def __init__(self, kode, judul, tahun, penulis, penerbit): 
        super().__init__(kode, judul, tahun) 
        self.penulis = penulis 
        self.penerbit = penerbit 
 
    def display_info(self): 
        return f"Buku: [{self.kode}] {self.judul} ({self.tahun}) oleh {self.penulis}, Penerbit: {self.penerbit}" 
 
class Majalah(Koleksi): 
    def __init__(self, kode, judul, tahun, penerbit, edisi): 
        super().__init__(kode, judul, tahun) 
        self.penerbit = penerbit 
        self.edisi = edisi 
 
    def display_info(self): 
        return f"Majalah: [{self.kode}] {self.judul} ({self.tahun}), Edisi: {self.edisi}, Penerbit: {self.penerbit}" 
 
class Jurnal(Koleksi): 
    def __init__(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor): 
        super().__init__(kode, judul, tahun) 
        self.penerbit = penerbit 
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor 
 
    def display_info(self): 
        return f"Jurnal: [{self.kode}] {self.judul} ({self.tahun}), Bidang:{self.bidang_studi}, Impact Factor: {self.impact_factor}, Penerbit: {self.penerbit}" 
 
class Perpustakaan: 
    def __init__(self): 
        self.koleksi = [] 
 
    def tambah_koleksi(self): 
        print("=" * 50) 
        print("PILIH JENIS KOLEKSI YANG AKAN DITAMBAH".center(50)) 
        print("=" * 50)
        print("1. Buku") 
        print("2. Majalah") 
        print("3. Jurnal") 
        print("=" * 50) 
 
        try: 
            jenis = int(input("Masukkan nomor pilihan: ")) 
            if jenis not in [1, 2, 3]: 
                print("Pilihan tidak valid! Coba lagi.") 
                return 
 
            kode = input("Masukkan Kode Koleksi: ") 
            judul = input("Masukkan Judul: ") 
            tahun = input("Masukkan Tahun Terbit: ") 
 
            if jenis == 1: 
                penulis = input("Masukkan Penulis: ") 
                penerbit = input("Masukkan Penerbit: ") 
                self.koleksi.append(Buku(kode, judul, tahun, penulis, penerbit)) 
            elif jenis == 2: 
                penerbit = input("Masukkan Penerbit: ") 
                edisi = input("Masukkan Edisi: ") 
                self.koleksi.append(Majalah(kode, judul, tahun, penerbit, edisi)) 
            elif jenis == 3: 
                penerbit = input("Masukkan Penerbit: ") 
                bidang_studi = input("Masukkan Bidang Studi: ") 
                impact_factor = input("Masukkan Impact Factor: ") 
                self.koleksi.append(Jurnal(kode, judul, tahun, penerbit, bidang_studi, impact_factor)) 
 
            print("Koleksi berhasil ditambahkan!") 
        except ValueError: 
            print("Masukkan angka yang valid!")     
    
    def tampilkan_koleksi(self): 
        print("=" * 50) 
        print("DAFTAR SEMUA KOLEKSI".center(50)) 
        print("=" * 50) 
         
        if not self.koleksi: 
            print("⚠ Tidak ada koleksi di perpustakaan.") 
        else: 
            for i, item in enumerate(self.koleksi, start=1): 
                print(f"Koleksi {i}:") 
                print(item)  
                print("-" * 50) 
 
    def hapus_koleksi(self): 
        print("=" * 50) 
        print("HAPUS DATA KOLEKSI".center(50)) 
        print("=" * 50) 
        kode = input("Masukkan kode koleksi yang ingin dihapus: ") 
         
        for koleksi in self.koleksi: 
            if koleksi.kode == kode: 
                self.koleksi.remove(koleksi) 
                print("   Koleksi berhasil dihapus!") 
                return 
         
        print("Kode koleksi tidak ditemukan!") 
 
def main(): 
    perpustakaan = Perpustakaan() 
    print("    Selamat datang di LIBRANOTE!    ".center(50)) 
 
    while True: 
        print("=" * 50) 
        print(" MENU PROGRAM".center(50)) 
        print("=" * 50) 
        print("1. Tambah koleksi  ") 
        print("2. Tampilkan semua koleksi       ") 
        print("3. Hapus koleksi    ") 
        print("4. Keluar  ") 
        print("=" * 50) 
         
        try: 
            pilihan = int(input("Masukkan nomor pilihan: ")) 
            if pilihan == 1: 
                perpustakaan.tambah_koleksi() 
            elif pilihan == 2: 
                perpustakaan.tampilkan_koleksi() 
            elif pilihan == 3:
                 perpustakaan.hapus_koleksi() 
            elif pilihan == 4: 
                print(" Terima kasih telah menggunakan LIBRANOTE! Silakan kembali lagi.") 
                break 
            else: 
                print("⚠ Pilihan tidak valid! Coba lagi.") 
        except ValueError: 
            print("⚠ Masukkan angka yang valid!") 
 
main()