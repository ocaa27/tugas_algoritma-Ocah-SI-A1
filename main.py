# Program Aplikasi Kasir Restoran

def main():
    # 1. Mulai Program & Inisialisasi Menu
    menu = {
        1: ("Nasi Goreng", 25000),
        2: ("Mie Ayam", 15000),
        3: ("Ayam Geprek", 20000),
        4: ("Sate Ayam", 30000),
        5: ("Bakso", 18000)
    }

    total = 0
    pesanan_list = []

    print("==========================================")
    print("      KONSEP APLIKASI KASIR RESTORAN      ")
    print("==========================================")

    # Loop pemilihan menu
    while True:
        # 2. Tampilkan Menu Makanan
        print("\nDaftar Menu Makanan:")
        for nomor, (nama, harga) in menu.items():
            print(f"{nomor}. {nama:<12} - Rp{harga:,}".replace(',', '.'))
        print("0. Selesai Memilih")
        print("------------------------------------------")

        try:
            pilihan = int(input("Pilih menu (0-5): "))
        except ValueError:
            print("Pilihan harus berupa angka!")
            continue

        # 4. Apakah Pilihan 0? (Cek Selesai Memilih)
        if pilihan == 0:
            break

        # 3. Proses Pemesanan
        if pilihan in menu:
            nama_makanan, harga_makanan = menu[pilihan]
            jumlah = int(input(f"Masukkan jumlah pesanan untuk {nama_makanan}: "))
            subtotal = harga_makanan * jumlah
            total += subtotal
            pesanan_list.append((nama_makanan, harga_makanan, jumlah, subtotal))
            print(f"-> Ditambahkan: {nama_makanan} x{jumlah} = Rp{subtotal:,}".replace(',', '.'))
        else:
            print("Pilihan menu tidak valid, silakan coba lagi.")

    # 5. Hitung Diskon
    if total > 200000:
        persen_diskon = 20
        potongan = total * 0.20
    else:
        persen_diskon = 0
        potongan = 0

    total_bayar = total - potongan

    # 6. Tampilkan Struk Pembayaran
    print("\n" + "="*40)
    print("         STRUK PEMBAYARAN RESTORAN        ")
    print("="*40)
    if pesanan_list:
        for nama, harga, jumlah, subtotal in pesanan_list:
            print(f"{nama:<15} x{jumlah:<2} Rp{subtotal:>10,}".replace(',', '.'))
        print("-" * 40)
    
    print(f"Total Belanja : Rp{total:>12,}".replace(',', '.'))
    print(f"Diskon        : {persen_diskon:>12}%")
    print(f"Potongan      : Rp{potongan:>12,.0f}".replace(',', '.'))
    print("-" * 40)
    print(f"Total Bayar   : Rp{total_bayar:>12,.0f}".replace(',', '.'))
    print("="*40)
    print("     Terima Kasih atas Kunjungan Anda!    ")
    print("="*40)

if __name__ == "__main__":
    main()
