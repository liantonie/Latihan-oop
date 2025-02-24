#Latihan 6
#Membuat kelas
class Segitiga:
  #membuat konstruktor
  def __init__(self, __alas, __tinggi):
    self.__alas = __alas
    self.__tinggi = __tinggi
  
  #membuat property method dengan set dan get
  def setAlas(self, __alas):
    self.__alas = __alas
  def getAlas(self):
    return self.__alas
  
  def setTinggi(self, __tinggi):
    self.__tinggi = __tinggi
  def getTinggi(self):
    return self.__tinggi

  #membuat method dengan fungsi tanpa parameter
  def hitung(self):
    return 0.5 * self.__alas * self.__tinggi
  
  #program utama
  def main():
    #instansiasi kelas menjadi objek
    objSegitiga = Segitiga(None, None)

    objSegitiga.setAlas(int(input("Masukkan alas \t: ")))
    objSegitiga.setTinggi(int(input("Masukkan tinggi : ")))
    print("Luas segitiga\t:", objSegitiga.hitung())
  main()