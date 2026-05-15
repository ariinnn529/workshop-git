# Program Menghitung Luas Bangun Datar

print("Hitung Luas :")
print("1. Lingkaran")
print("2. Segitiga")
print("3. Jajar Genjang")
print("4. Trapesium")

pilihan = int(input("Pilih menu (1-4): "))

# 1. Lingkaran
if pilihan == 1:
    r = float(input("Masukkan jari-jari: "))
    luas = 3.14 * r * r
    print("Luas Lingkaran =", luas)

# 2. Segitiga
elif pilihan == 2:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Luas Segitiga =", luas)

# 3. Jajar Genjang
elif pilihan == 3:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = alas * tinggi
    print("Luas Jajar Genjang =", luas)

# 4. Trapesium
elif pilihan == 4:
    sisi_a = float(input("Masukkan sisi atas: "))
    sisi_b = float(input("Masukkan sisi bawah: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * (sisi_a + sisi_b) * tinggi
    print("Luas Trapesium =", luas)

else:
    print("Pilihan tidak tersedia")