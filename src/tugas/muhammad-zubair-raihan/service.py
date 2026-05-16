import math

# Persegi Panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari**2

# Segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Jajar Genjang
def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

# Trapesium
def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    return 0.5 * (sisi_atas + sisi_bawah) * tinggi

# Contoh penggunaan:
print("Luas Persegi Panjang:", luas_persegi_panjang(10, 5))
print("Luas Lingkaran:", luas_lingkaran(7))
print("Luas Segitiga:", luas_segitiga(8, 6))
print("Luas Jajar Genjang:", luas_jajar_genjang(9, 4))
print("Luas Trapesium:", luas_trapesium(6, 10, 5))
