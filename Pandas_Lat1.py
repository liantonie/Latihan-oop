import pandas as pd

# Membuat DataFrame contoh
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Seleksi data menggunakan label
alice_data = df.loc[2]  # Mengakses baris pertama
age_city = df.loc[:, ['Age', 'City']]  # Mengakses kolom 'Age' dan 'City'

print(alice_data)
print(age_city)