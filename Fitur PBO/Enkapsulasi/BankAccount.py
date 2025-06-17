class BankAccount:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal
 
    # Method getter untuk membaca saldo (tanpa bisa diubah langsung)
    def get_saldo(self):
        return self.__saldo
     
    # Method setter untuk memperbarui saldo dengan validasi
    def set_saldo(self, jumlah):
        if jumlah < 0:
            print("Jumlah saldo tidak boleh negatif!")
        else:
            self.__saldo = jumlah
            print(f"Saldo berhasil diperbarui menjadi: {self.__saldo}")
 
    # Metode untuk menambah saldo
    def deposit(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Saldo bertambah: {jumlah}, Saldo sekarang: {self.__saldo}")
        else:
            print("Jumlah deposit harus positif!")
 
    # Metode untuk menarik saldo
    def withdraw(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil menarik: {jumlah}, Saldo sekarang: {self.__saldo}")
        else:
            print("Penarikan gagal: saldo tidak mencukupi atau jumlah tidak valid")
 
# Contoh Penggunaan
akun = BankAccount("Budi", 1000)
print(akun.get_saldo())  # Output: 1000
 
akun.set_saldo(-2000)     # Update saldo
akun.deposit(500)        # Menambah saldo
akun.withdraw(1000)      # Menarik saldo
 
# Akses langsung ke atribut __saldo akan error
# print(akun.__saldo)   # AttributeError: 'BankAccount' object has no attribute '__saldo'