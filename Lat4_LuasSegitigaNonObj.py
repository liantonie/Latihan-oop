#Latihan 4
#Program: Menghitung luas segitiga
#membuat fungsi tanpa parameter
def hitung():
  alas= int(input("Masukkan alas \t: "))
  tinggi= int(input("Masukkan tinggi : "))

  luas =  0.5 * alas  * tinggi
  return luas

#program utama
def main():
    #memanggil fungsi
    print ("Luas segitiga\t:", hitung())
main()
