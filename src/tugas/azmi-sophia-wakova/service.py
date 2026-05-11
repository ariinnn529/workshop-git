def hitung_luas_persegi_panjang(panjang, lebar):
    """
    Fungsi untuk menghitung luas persegi panjang.
    Rumus: Luas = Panjang x Lebar
    """
    luas = panjang * lebar
    return luas

# Contoh penggunaan fungsi (opsional) yaitu:
if __name__ == "__main__":
    p = 10
    l = 5
    hasil = hitung_luas_persegi_panjang(p, l)
    print(f"Luas persegi panjang dengan panjang {p} dan lebar {l} adalah: {hasil}")