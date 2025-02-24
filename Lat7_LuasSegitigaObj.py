#Latihan 7
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self,alas,tinggi):
        self.alas =  alas
        self.tinggi =  tinggi
    
    #membuat method dengan fungsi tanpa parameter
    def hitung(self):
        return  0.5 * self.alas  * self.tinggi


#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None,None)
        
    objSegitiga.alas= int(input("Masukkan alas \t: "))
    objSegitiga.tinggi= int(input("Masukkan tinggi : "))
    print ("Luas segitiga\t:", objSegitiga.hitung())
main()
