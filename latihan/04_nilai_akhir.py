# Input data
nama = input("Nama: ")
tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

# Perhitungan nilai akhir dengan bobot 20%, 30%, dan 50%
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# Tampilan output
print(f"\nNama        : {nama}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")