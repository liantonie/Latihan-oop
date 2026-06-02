class Pelanggan:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = nama
        self.nomor_telepon = nomor_telepon
        self.email = email
    
    def tampil_info(self):
        print(f"Nama Pelanggan: {self.nama} - No. Telp: {self.nomor_telepon} - Email: {self.email}")

class Kamar:
    def __init__(self, nomor_kamar, tipe_kamar, harga_per_malam, tersedia):
        self.nomor_kamar = nomor_kamar
        self.tipe_kamar = tipe_kamar
        self.harga_per_malam = harga_per_malam
        self.tersedia = tersedia
    
    def tampilkan_info(self):
        print(f"{self.nomor_kamar} - {self.tipe_kamar} - {self.harga_per_malam} - {self.tersedia}")
    
    def ubah_status(self, ketersediaan):
        self.tersedia = ketersediaan

class ListKamar:
    def __init__(self):
        self.data_kamar = []
    
    def tambahkan_kamar(self, kamar):
        self.data_kamar.append(kamar)
    
    def tampilkan_data_kamar(self):
        for data in self.data_kamar:
            print(f"{data.nomor_kamar} - {data.tipe_kamar} - {data.harga_per_malam} - {data.tersedia}")

class Reservasi:
    def __init__(self, pelanggan, nomor_kamar, data_kamar, jumlah_malam):
        self.pelanggan = pelanggan
        self.nomor_kamar = nomor_kamar
        self.jumlah_malam = jumlah_malam
        self.data_kamar = data_kamar
    
    def hitungTotal(self):

        totalBiaya = 0
        for kamar in self.data_kamar:
            if kamar.nomor_kamar == self.nomor_kamar:
                totalBiaya = kamar.harga_per_malam * self.jumlah_malam
                break

        print(f"Hello {self.pelanggan.nama},  total biaya menginap: Rp {totalBiaya}")


# membuat data pelanggan
p1 = Pelanggan("Budiman", "0857191881", "budiman@gmail.com")
# menampilkan data pelanggan
p1.tampil_info()

# membuat data kamar
dataKamar = ListKamar()

# membuat kamar dan menambahkannya dalam data kamar
k1 = Kamar("01", "standar", 200000, 1)
dataKamar.tambahkan_kamar(k1)
k2 = Kamar("02", "deluxe", 300000, 1)
dataKamar.tambahkan_kamar(k2)
k3 = Kamar("03", "suite", 500000, 1)
dataKamar.tambahkan_kamar(k3)

# mengubah status ketersediaan kamar tertentu
k3.ubah_status(0)

# menampilkan semua data kamar
dataKamar.tampilkan_data_kamar()

# membuat reservasi kamar
r1 = Reservasi(p1, "02", dataKamar.data_kamar, 5)

# menghitung total reservasi
r1.hitungTotal()
