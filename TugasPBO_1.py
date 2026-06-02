#Kelas Abstrak untuk attribut utama buku, majalah, jurnal
from abc import ABC, abstractmethod

class Perpus(ABC):
    def __init__(self, kode, judul, tahun, penerbit):
        self.kode=kode
        self.judul=judul
        self.tahun=tahun
        self.penerbit=penerbit
    @abstractmethod
    def show_info(self):
        pass

#Kelas Buku yang menrupakan turunan dari kelas Perpus
class Buku(Perpus):
    def __init__(self, kode, judul, tahun, penerbit, pengarang):
        super().__init__(kode, judul, tahun, penerbit)
        self.pengarang=pengarang
    def show_info(self):
        print("Jenis        : Buku")
        print(f"Kode Koleksi : {self.kode}")
        print(f"Judul        : {self.judul}")
        print(f"Tahun Terbit : {self.tahun}")
        print(f"Pengarang    : {self.pengarang}")
        print(f"Penerbit     : {self.penerbit}")

#Kelas Majalah yang menrupakan turunan dari kelas Perpus
class Majalah(Perpus):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun, penerbit)
        self.edisi=edisi
    def show_info(self):
        print("Jenis        : Majalah")
        print(f"Kode Koleksi : {self.kode}")
        print(f"Judul        : {self.judul}")
        print(f"Tahun Terbit : {self.tahun}")
        print(f"Penerbit     : {self.penerbit}")
        print(f"Edisi        : {self.edisi}")
        
#Kelas Jurnal yang menrupakan turunan dari kelas Perpus
class Jurnal(Perpus):
    def __init__(self, kode, judul, tahun, penerbit, bidang, factor):
        super().__init__(kode, judul, tahun, penerbit)
        self.bidang=bidang
        self.factor=factor
    def show_info(self):
        print("Jenis        : Jurnal")
        print(f"Kode Koleksi : {self.kode}")
        print(f"Judul        : {self.judul}")
        print(f"Tahun Terbit : {self.tahun}")
        print(f"Penerbit     : {self.penerbit}")
        print(f"Bidang studi : {self.bidang}")
        print(f"Impact Factor: {self.factor}")

#Kelas untuk manajemen perpustakaan
class Library:
    def __init__(self):
        self.koleksi=[]
        pass

    def tambah(self, publikasi):
        self.koleksi.append(publikasi)
    
    def hapus(self,kode):
        for publikasi in self.koleksi:
            if publikasi.kode == kode:
                self.koleksi.remove(publikasi)
                print("------------------------------")
                print("   KOLEKSI BERHASIL DIHAPUS   ")
                print("------------------------------")
                return
        print("Data tidak ditemukan")
    
    def tampil(self):
        if not self.koleksi:
            print ("Koleksi Kosong!")
        else:
            for i, publikasi in enumerate(self.koleksi, start=1):
                print(f"Koleksi {i}:")
                publikasi.show_info()
                print()

#Program utama
def main():
    perpustakaan=Library()

    while True:
        print("================================")
        print("          MENU PROGRAM          ")
        print("--------------------------------")
        print("1. Tambah data koleksi")
        print("2. Hapus data koleksi")
        print("3. Tampil semua data koleksi")
        print("4. Keluar")
        menu=int(input("nomer yang anda pilih: "))
        print("")

        if menu==1:
            print("================================")
            print("Jenis Koleksi Yang akan ditambah")
            print("--------------------------------")
            print("1. Buku")
            print("2. Majalah")
            print("3. Jurnal")
            add=int(input("nomer yang anda pilih: "))
            print("")
            if add==1:
                print("------------------------------")
                print("       TAMBAH DATA BUKU       ")
                print("------------------------------")
                kode=input("Masukan Kode buku     :")
                judul=input("Masukan judul buku    :")
                tahun=input("Masukan tahun terbit  :")
                penerbit=input("Masukan penerbit      :")
                pengarang=input("Masukan pengarang     :")
                book=Buku(kode,judul,tahun,penerbit,pengarang)
                perpustakaan.tambah(book)
                print("------------------------------")
                print("   BUKU BERHASIL DITAMBAHKAN  ")
                print("------------------------------")
            elif add==2:
                print("------------------------------")
                print("     TAMBAH DATA MAJALAH      ")
                print("------------------------------")
                kode=input("Masukan Kode majalah  :")
                judul=input("Masukan judul majalah :")
                tahun=input("Masukan tahun terbit  :")
                penerbit=input("Masukan penerbit      :")
                edisi=input("Masukan edisi         :")
                magazine=Majalah(kode,judul,tahun,penerbit,edisi)
                perpustakaan.tambah(magazine)
                print("------------------------------")
                print(" MAJALAH BERHASIL DITAMBAHKAN ")
                print("------------------------------")
            elif add==3:
                print("------------------------------")
                print("      TAMBAH DATA JURNAL      ")
                print("------------------------------")
                kode=input      ("Masukan Kode jurnal   :")
                judul=input     ("Masukan judul jurnal  :")
                tahun=input     ("Masukan tahun jurnal  :")
                penerbit=input  ("Masukan penerbit      :")
                bidang=input    ("Masukan bidang studi  :")
                factor=input("Masukan Impact Factor :")
                journal=Jurnal(kode,judul,tahun,penerbit,bidang,factor)
                perpustakaan.tambah(journal)
                print("------------------------------")
                print(" JURNAL BERHASIL DITAMBAHKAN  ")
                print("------------------------------")
            else:
                print("Tidak ada pilihan dalam menu\n")

        elif menu==2:
            print("------------------------------")
            print("        HAPUS KOLEKSI         ")
            print("------------------------------")
            remove=input("Masukan kode Koleksi  :")
            perpustakaan.hapus(remove)

        elif menu==3:
            print("------------------------------")
            print("         DATA KOLEKSI         ")
            print("------------------------------\n")
            perpustakaan.tampil()

        elif menu==4:
            print("Program selesai, Terima Kasih. XD")
            break
        else:
            print("Tidak ada pilihan dalam menu!")
    input("\nTekan [Enter] untuk kembali ke menu...")
main()
