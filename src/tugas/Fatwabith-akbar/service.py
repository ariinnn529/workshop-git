def hitung_luas(panjang, lebar):
    """Fungsi untuk menghitung luas persegi panjang"""
    return panjang * lebar

if __name__ == "__main__":
    # Definisi variabel
    Panjang = 10
    Lebar = 5

    # Perhitungan Luas
    Luas = hitung_luas(Panjang, Lebar)

    # Menampilkan hasil
    print(f"Luas = {Luas}")
