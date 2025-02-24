#Latihan 2
#Program : Menghitung luas segitiga
#Membuat prosedur tanpa parameter
def hitung():
  alas = int(input("Masukkan alas \t: "))
  tinggi = int(input("Masukkan tinggi : "))

  luas = 0.5 * alas * tinggi
  print ("Luas segitiga \t:", luas)

#program utama
def main():
  #memanggil prosedur
  hitung()
main()