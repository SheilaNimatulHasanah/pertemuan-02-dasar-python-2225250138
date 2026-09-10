"""
Program: Kalkulator Koordinat Dua Titik
Identitas: Sheila Ni'matul Hasanah | NIM: 2225250138 | Kelas: 3B
Deskripsi: Menghitung perubahan koordinat, jarak Euclidean, dan titik tengah
          antara dua titik (A dan B) tanpa fungsi buatan sendiri atau pustaka eksternal.
"""

print("KALKULATOR KOORDINAT DUA TITIK")

# Input titik A dan B
x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

# Perhitungan koordinat
dx = x2 - x1
dy = y2 - y1
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

# Tampilan hasil dengan format 2 angka desimal
print(f"\nTitik A       : ({x1:.2f}, {y1:.2f})")
print(f"Titik B       : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan     : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B  : {jarak:.2f}")
print(f"Titik tengah  : ({mid_x:.2f}, {mid_y:.2f})")