class Kotak:
    def luas(self, panjang, lebar):
        return panjang * lebar

class Segitiga:
    def luas(self, alas, tinggi):
        return 0.5 * alas * tinggi

def hitung_luas(bentuk):
    print("Luas:", bentuk.luas(4, 5))

def main():
    kotak = Kotak()
    segitiga = Segitiga()

    hitung_luas(kotak)
    hitung_luas(segitiga)

main()