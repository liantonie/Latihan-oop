#Latihan 5
#Program: Menghitung luas segitiga
#membuat fungsi dengan parameter
def hitung(alas, tinggi):
    luas =  0.5 * alas  * tinggi
    return luas
       
#program utama
def main():
    alas= int(input("Masukkan alas \t: "))
    tinggi= int(input("Masukkan tinggi : "))

    #memanggil fungsi
    print ("Luas segitiga\t:", hitung(alas, tinggi))
main()
