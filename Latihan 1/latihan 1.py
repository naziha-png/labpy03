# latihan1.py
# Menampilkan n bilangan acak yang lebih kecil dari 0.5

from random import random

n = int(input("Masukkan jumlah bilangan acak: "))
print("\nBilangan acak yang lebih kecil dari 0.5:")

for i in range(n):
    a = random()
    if a < 0.5:
        print(f"Data ke-{i+1}: {a}")
