class Kucing:
    def bersuara(self):
        print("Meow")

class Anjing:
    def bersuara(self):
        print("Woof")

def main():
    kucing = Kucing()
    anjing = Anjing()


    kucing.bersuara() # Memanggil metode yang sama pada objek yang berbeda

main()