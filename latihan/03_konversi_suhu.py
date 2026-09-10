KELVIN_OFFSET = 273.15

# Input suhu Celsius
celsius = float(input("Masukkan suhu Celsius: "))

# Perhitungan
fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

# Tampilan output
print(f"Fahrenheit : {fahrenheit:.2f}")
print(f"Kelvin     : {kelvin:.2f}")