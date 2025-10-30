# latihan2.py
# Menghitung total keuntungan selama 8 bulan
modal_awal = 100_000_000
laba = 0
persentase = [0, 0, 1, 1, 5, 5, 5, 3]  # persen laba per bulan
print("Modal awal: Rp", modal_awal)
for i in range(8):
    bulan = i + 1
    keuntungan = modal_awal * persentase[i] / 100
    laba += keuntungan
    print(f"Bulan ke-{bulan} laba {persentase[i]}% = Rp {keuntungan:,.0f}")
print("\nTotal laba selama 8 bulan = Rp", f"{laba:,.0f}")