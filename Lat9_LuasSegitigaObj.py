#Latihan 9
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self,alas,tinggi):
        self.alas =  alas
        self.tinggi =  tinggi
    
    #membuat method dengan fungsi beserta parameter
    def hitung(self, alas, tinggi):
        return  0.5 * alas  * tinggi
       
#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
        
    objSegitiga.alas= int(input("Masukkan alas \t: "))
    objSegitiga.tinggi= int(input("Masukkan tinggi : "))
    print ("Luas segitiga\t:", objSegitiga.hitung(objSegitiga.alas, 
                                                  objSegitiga.tinggi))
main()
