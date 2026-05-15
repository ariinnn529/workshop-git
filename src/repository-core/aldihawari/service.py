import math

def hitung_luas_jajar_genjang(alas, tinggi):

    if alas <= 0 or tinggi <= 0:
        raise ValueError("Alas dan tinggi harus bernilai positif!")
    
    luas = alas * tinggi
    return luas


def main():
    print("=== Kalkulator Luas Jajar Genjang ===")
    print("Rumus: Luas = alas × tinggi\n")
    
    try:
        alas = float(input("Masukkan panjang alas (cm): "))
        tinggi = float(input("Masukkan tinggi (cm): "))
        
        luas = hitung_luas_jajar_genjang(alas, tinggi)
        
        print(f"\nHasil:")
        print(f"  Alas   = {alas} cm")
        print(f"  Tinggi = {tinggi} cm")
        print(f"  Luas   = {luas} cm²")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()