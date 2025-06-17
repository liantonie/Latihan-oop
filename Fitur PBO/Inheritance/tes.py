# superclass
class Karyawan:
    nik = ""
    nama = ""
     
    def gajiPokok(self):
        return 3000000
     
    def printData(self):
        print("NIK: ", self.nik)
        print("Nama: ", self.nama)
        print("Gaji Pokok: ", self.gajiPokok())
     
 
# subclass Dosen mewarisi Karyawan
class Dosen(Karyawan):
    nidn = ""
     
    def tunjangan(self):
        return 2000000
     
    # overriding
    def printData(self):
        print("NIK: ", self.nik)
        print("Nama: ", self.nama)
        print("NIDN: ", self.nidn)
        print("Gaji Pokok: ", self.gajiPokok())
        print("Tunjangan: ", self.tunjangan())


karyawan1 = Karyawan()
 
karyawan1.nik = "K01"
karyawan1.nama = "Budi"
karyawan1.printData()


karyawan2 = Dosen()
 
karyawan2.nik = "K01"
karyawan2.nama = "Budi"
karyawan2.nidn = "123"
karyawan2.printData()
 