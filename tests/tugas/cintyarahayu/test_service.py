import unittest
from src.tugas.cintyarahayu.service import hitung_luas_trapesium

class TestService(unittest.TestCase):
    def test_hitung_luas_trapesium(self):
        # Kasus 1: Angka positif
        # (5 + 7) * 4 / 2 = 12 * 4 / 2 = 24
        self.assertEqual(hitung_luas_trapesium(5, 7, 4), 24.0)
        
        # Kasus 2: Angka desimal
        # (2.5 + 3.5) * 2 / 2 = 6 * 1 = 6
        self.assertEqual(hitung_luas_trapesium(2.5, 3.5, 2), 6.0)
        
        # Kasus 3: Tinggi nol
        self.assertEqual(hitung_luas_trapesium(10, 5, 0), 0.0)
        
        # Kasus 4: Alas nol
        self.assertEqual(hitung_luas_trapesium(0, 0, 10), 0.0)

if __name__ == '__main__':
    unittest.main()
