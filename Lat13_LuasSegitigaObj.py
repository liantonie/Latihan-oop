#Latihan 13
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self,alas,tinggi):
        self.alas =  alas
        self.tinggi =  tinggi
    
    #membuat method dengan fungsi tanpa nilai balik/prosedur
    #beserta parameter
    def hitung(self, alas, tinggi):
      luas = 0.5 * alas  * tinggi
      print ("Luas segitiga\t:", luas)

#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
        
    objSegitiga.alas= int(input("Masukkan alas \t: "))
    objSegitiga.tinggi= int(input("Masukkan tinggi : "))
    objSegitiga.hitung(objSegitiga.alas, objSegitiga.tinggi)
main()
