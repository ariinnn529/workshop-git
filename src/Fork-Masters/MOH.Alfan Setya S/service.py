def hitung_luas_trapesium(sisi_a, sisi_b, tinggi):
    luas = 0.5 * (sisi_a + sisi_b) * tinggi
    return luas

sisi_a = 5
sisi_b = 7
tinggi = 4
hasil = hitung_luas_trapesium(sisi_a, sisi_b, tinggi)
print(f"Luas trapesium dengan sisi sejajar {sisi_a} dan {sisi_b}, serta tinggi {tinggi} adalah: {hasil}")