# superclass
class Karyawan:
     
    # constructor
    def __init__(self, nik, nama):
        self.nik = nik
        self.nama = nama
     
    def gajiPokok(self):
        return 3000000
     
    def printData(self):
        print("NIK: ", self.nik)
        print("Nama: ", self.nama)
        print("Gaji Pokok: ", self.gajiPokok())


class Dosen(Karyawan):
     
    # constructor
    def __init__(self, nik, nama, nidn):
        # memanggil constructor superclass
        super().__init__(nik, nama)
        self.nidn = nidn
     
    def tunjangan(self):
        return 2000000
     
    # overriding
    def printData(self):
        print("NIK: ", self.nik)
        print("Nama: ", self.nama)
        print("NIDN: ", self.nidn)
        print("Gaji Pokok: ", self.gajiPokok())
        print("Tunjangan: ", self.tunjangan())


karyawan1 = Karyawan("K01", "Budi")
karyawan1.printData()

karyawan2 = Dosen("K01", "Budi", "123")
karyawan2.printData()

