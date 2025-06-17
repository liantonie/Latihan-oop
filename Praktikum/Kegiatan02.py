
class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    def tampilkan_info(self):  
        print(f"Produk: {self.nama}, Harga: {self.harga}") 
    
    def diskon(self, persen):
        diskon_harga = self.harga * (persen / 100)
        return self.harga - diskon_harga  

# Pembuatan objek dan pemanggilan method
produk1 = Produk("Laptop", 15000000)
produk1.tampilkan_info() 

harga_setelah_diskon = produk1.diskon(10)
print(f"Harga setelah diskon: {harga_setelah_diskon}")
