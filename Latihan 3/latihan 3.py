# latihan3.py
# Simulasi mesin ATM sederhana
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