#Latihan 11
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self,alas,tinggi):
        self.alas =  alas
        self.tinggi =  tinggi
    
    #membuat method dengan fungsi tanpa nilai balik/prosedur
    #tanpa parameter
    def hitung(self):
        luas =  0.5 * self.alas  * self.tinggi
        print ("Luas segitiga\t:", luas)
       
#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
        
    objSegitiga.alas= int(input("Masukkan alas \t: "))
    objSegitiga.tinggi= int(input("Masukkan tinggi : "))
    objSegitiga.hitung()
main()
