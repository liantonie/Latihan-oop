def cek_suhu(suhu):
    if suhu > 30:
        return "Panas"
    elif suhu >= 20:
        return "Sejuk"
    else:
        return "Dingin"

# Program utama
suhu_input = int(input("Masukkan suhu dalam derajat Celsius: "))
hasil = cek_suhu(suhu_input)
print("Cuaca hari ini:", hasil)