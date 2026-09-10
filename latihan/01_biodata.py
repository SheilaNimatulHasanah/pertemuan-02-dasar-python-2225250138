# Konstanta
TAHUN_SEKARANG = 2026

# Input data
nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

# Perhitungan
umur = TAHUN_SEKARANG - tahun_lahir

# Tampilan output
print(f"\nNama  : {nama}")
print(f"NIM   : {nim}")
print(f"Kelas : {kelas}")
print(f"Umur  : sekitar {umur} tahun")