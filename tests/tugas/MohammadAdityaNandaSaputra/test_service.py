import unittest

from src.tugas.MohammadAdityaNandaSaputra.service import luas_persegi_panjang

class TestLuas(unittest.TestCase):
    def test_luas(self):
        hasil = luas_persegi_panjang(5, 5)
        self.assertEqual(hasil, 25)