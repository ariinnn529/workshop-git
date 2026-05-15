import math

def hitung_luas_lingkaran(jari_jari):
    if jari_jari < 0:
        raise ValueError("Jari-jari tidak boleh negatif")
    return math.pi * (jari_jari ** 2)
