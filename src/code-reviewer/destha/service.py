def hitung_luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    """
    Fungsi untuk menghitung luas trapesium.
    Rumus: Luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    """
    luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    return luas

if __name__ == "__main__":
    print("=== PROGRAM HITUNG LUAS TRAPESIUM ===")
    try:
        a = float(input("Masukkan panjang sisi atas (a): "))
        b = float(input("Masukkan panjang sisi bawah (b): "))
        t = float(input("Masukkan tinggi trapesium (t): "))
        
        hasil = hitung_luas_trapesium(a, b, t)
        
        print("-" * 37)
        print(f"Sisi Atas  : {a}")
        print(f"Sisi Bawah : {b}")
        print(f"Tinggi     : {t}")
        print("-" * 37)
        print(f"Luas Trapesium adalah: {hasil}")
        print("=====================================")
    except ValueError:
        print("Error: Harap masukkan angka yang valid!")
