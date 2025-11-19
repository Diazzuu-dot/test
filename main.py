# 1. Impor library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# 2. Siapkan data untuk sumbu-x
# Membuat 400 titik dari 0.01 sampai 3 agar kurva terlihat mulus
x_values = np.linspace(0.01, 3, 400)

# 3. Hitung data untuk sumbu-y sesuai rumus
y_ln = np.log(x_values)      # Kurva y = ln(x)
y_exp = np.exp(-x_values)    # Kurva y = e^(-x)

# 4. Gambar kedua kurva pada plot yang sama
plt.plot(x_values, y_ln, label='y = ln(x)')
plt.plot(x_values, y_exp, label='y = e^{-x}')

# 5. Tambahkan detail agar grafik mudah dibaca
plt.title('Grafik y = ln(x) dan y = e^{-x}') # Judul
plt.xlabel('Sumbu-X')                      # Label sumbu-x
plt.ylabel('Sumbu-Y')                      # Label sumbu-y
plt.legend()                               # Keterangan kurva
plt.grid(True)                             # Garis bantu (grid)
plt.axhline(0, color='black', linewidth=0.5) # Garis sumbu-x
plt.axvline(0, color='black', linewidth=0.5) # Garis sumbu-y

# 6. Simpan grafik ke dalam sebuah file
plt.savefig('grafik_perpotongan.png')

# print("Grafik telah disimpan sebagai 'grafik_perpotongan.png'")