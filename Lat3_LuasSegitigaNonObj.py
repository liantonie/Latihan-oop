#Latihan 3
#Program: Menghitung luas segitiga
#membuat prosedur dengan parameter
def hitung(alas, tinggi):
    luas =  0.5 * alas  * tinggi
    print ("Luas segitiga\t:", luas)
       
#Program utama
def main():
    #memanggil prosedur
    alas= int(input("Masukkan alas \t: "))
    tinggi= int(input("Masukkan tinggi : "))
    hitung(alas, tinggi)
main()