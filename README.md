
  # **LAPORAN PRAKTIKUM 3**  
  
  **Nama:** Naziha Raiqi Aribino  
  
  **Kelas:** TI.25.A2  
  
  **NIM:** 312510232  
  
 **Mata Kuliah:** Pengantar Pemrograman  
 
  **Topik:** Perulangan  
  

---

## **Tujuan Praktikum**

1. Mempelajari konsep perulangan `for` dan `while` dalam Python.
2. Mengimplementasikan pernyataan `break` dan `continue`.
3. Membuat program sederhana menggunakan perulangan.

---

## **LATIHAN 1 – Menampilkan Bilangan Acak**

### **Kode Program (latihan1.py)**

```python
from random import random

n = int(input("Masukkan jumlah bilangan acak: "))
print("\nBilangan acak yang lebih kecil dari 0.5:")

for i in range(n):
    a = random()
    if a < 0.5:
        print(f"Data ke-{i+1}: {a}")
```

### **Penjelasan Alur Program**

1. Import fungsi `random()` dari library `random`.
2. Input jumlah bilangan acak (`n`).
3. Gunakan perulangan `for` untuk menghasilkan `n` bilangan acak.
4. Tampilkan hanya bilangan yang **kurang dari 0.5**.

### **Contoh Hasil Run**

```
Masukkan jumlah bilangan acak: 10
Bilangan acak yang lebih kecil dari 0.5:
Data ke-1: 0.372828
Data ke-3: 0.128492
Data ke-6: 0.492051
```

---

## **LATIHAN 2 – Menghitung Total Laba 8 Bulan**

### **Kode Program (latihan2.py)**

```python
modal_awal = 100_000_000
laba = 0
persentase = [0, 0, 1, 1, 5, 5, 5, 3]

print("Modal awal: Rp", modal_awal)
for i in range(8):
    bulan = i + 1
    keuntungan = modal_awal * persentase[i] / 100
    laba += keuntungan
    print(f"Bulan ke-{bulan} laba {persentase[i]}% = Rp {keuntungan:,.0f}")

print("\nTotal laba selama 8 bulan = Rp", f"{laba:,.0f}")
```

### **Penjelasan Alur Program**

1. Tentukan `modal_awal = 100 juta`.
2. Buat list `persentase` berisi nilai laba tiap bulan.
3. Gunakan perulangan `for` untuk menghitung laba tiap bulan.
4. Akumulasi semua laba menjadi `total laba`.

### **Contoh Hasil Run**

```
Modal awal: Rp 100000000
Bulan ke-1 laba 0% = Rp 0
Bulan ke-2 laba 0% = Rp 0
Bulan ke-3 laba 1% = Rp 1,000,000
Bulan ke-4 laba 1% = Rp 1,000,000
Bulan ke-5 laba 5% = Rp 5,000,000
Bulan ke-6 laba 5% = Rp 5,000,000
Bulan ke-7 laba 5% = Rp 5,000,000
Bulan ke-8 laba 3% = Rp 3,000,000

Total laba selama 8 bulan = Rp 21,000,000
```

---

## **LATIHAN 3 – Simulasi Mesin ATM**

### **Kode Program (latihan3.py)**

```python
saldo = 1_000_000

while True:
    print("\n=== MENU ATM ===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print(f"Saldo Anda saat ini: Rp {saldo:,}")

    elif pilihan == "2":
        tarik = int(input("Masukkan jumlah penarikan: "))
        if tarik > saldo:
            print("Saldo tidak mencukupi!")
        else:
            saldo -= tarik
            print(f"Penarikan berhasil. Sisa saldo: Rp {saldo:,}")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan ATM ini.")
        break

    else:
        print("Menu tidak valid, silakan coba lagi.")
```

### **Penjelasan Alur Program**

1. Inisialisasi saldo awal Rp 1.000.000.
2. Gunakan `while True` untuk menampilkan menu berulang.
3. Jika pengguna memilih:

   * `1`: Menampilkan saldo.
   * `2`: Memasukkan jumlah penarikan, cek saldo, lalu kurangi saldo.
   * `3`: Keluar dari program.
4. Gunakan `break` untuk menghentikan perulangan saat memilih keluar.

### **Contoh Hasil Run**

```
=== MENU ATM ===
1. Cek Saldo
2. Tarik Tunai
3. Keluar
Pilih menu: 1
Saldo Anda saat ini: Rp 1,000,000

Pilih menu: 2
Masukkan jumlah penarikan: 300000
Penarikan berhasil. Sisa saldo: Rp 700,000

Pilih menu: 3
Terima kasih telah menggunakan ATM ini.
```

---

### **Kesimpulan**

Dari praktikum ini dapat disimpulkan bahwa:

* Perulangan `for` digunakan untuk jumlah iterasi yang sudah pasti.
* Perulangan `while` digunakan untuk kondisi yang tidak tentu.
* Pernyataan `break` menghentikan perulangan, sedangkan `continue` melewati satu iterasi dan melanjutkan ke iterasi berikutnya.
* Penerapan perulangan sangat berguna untuk memproses data berulang seperti perhitungan laba, simulasi sistem, dan pemrosesan otomatis.



