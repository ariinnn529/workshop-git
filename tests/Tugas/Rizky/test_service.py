import unittest

from src.Tugas.Rizky.service import luas_persegi_panjang

class TestLuasPersegiPanjang(unittest.TestCase):
    
    def test_luas_persegi_panjang_positif(self):
        hasil = luas_persegi_panjang(5, 3)
        self.assertEqual(hasil, 15)
        
    def test_luas_persegi_panjang_negatif(self):
        hasil = luas_persegi_panjang(-2, -3)
        self.assertEqual(hasil, 6)
        
    def test_luas_persegi_panjang_positif_dan_negatif(self):
        hasil = luas_persegi_panjang(4, -5)
        self.assertEqual(hasil, -20)        
        
    def test_luas_persegi_panjang_dengan_nol(self):
        hasil = luas_persegi_panjang(0, 4)
        self.assertEqual(hasil, 0)