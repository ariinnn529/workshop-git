import math

def hitung_luas_lingkaran(jari_jari):
    """
    Menghitung luas lingkaran berdasarkan jari-jari yang diberikan.
    Rumus: Luas = pi * r^2
    """
    if jari_jari < 0:
        return "Jari-jari tidak boleh negatif"
    
    luas = math.pi * (jari_jari ** 2)
    return luas

# Contoh penggunaan:
jari_jari = 7
hasil = hitung_luas_lingkaran(jari_jari)

print(f"Jari-jari: {jari_jari}")
print(f"Luas Lingkaran: {hasil:.2f}")
