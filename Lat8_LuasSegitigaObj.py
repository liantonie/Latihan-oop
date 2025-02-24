#Latihan 8
#membuat kelas
class Segitiga:
    #membuat konstruktor
    def __init__(self,__alas, __tinggi):
        self.__alas =  __alas
        self.__tinggi =  __tinggi
    
    #menerapkan property method dengan set dan get
    def setAlas(self, __alas):
        self.__alas =  __alas
    def getAlas(self):
        return self.__alas

    def setTinggi(self, __tinggi):
        self.__tinggi =  __tinggi
    def getTinggi(self):
        return self.__tinggi

    #membuat method dengan fungsi beserta parameter
    def hitung(self, alas, tinggi):
        return  0.5 * alas  * tinggi
       
#program utama
def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)
        
    objSegitiga.setAlas(int(input("Masukkan alas \t: ")))
    objSegitiga.setTinggi(int(input("Masukkan tinggi : ")))
    print ("Luas segitiga\t:", objSegitiga.hitung(objSegitiga.getAlas(), 
                                                  objSegitiga.getTinggi()))
main()
