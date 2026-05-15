import unittest
import math
from src.git_push.ajiputraprayogi.service import hitung_luas_lingkaran

class TestService(unittest.TestCase):
    def test_hitung_luas_lingkaran(self):
        # Kasus 1: Jari-jari positif
        # pi * 7^2 = pi * 49
        self.assertAlmostEqual(hitung_luas_lingkaran(7), math.pi * 49)
        
        # Kasus 2: Jari-jari desimal
        # pi * 2.5^2 = pi * 6.25
        self.assertAlmostEqual(hitung_luas_lingkaran(2.5), math.pi * 6.25)
        
        # Kasus 3: Jari-jari nol
        self.assertEqual(hitung_luas_lingkaran(0), 0.0)
        
        # Kasus 4: Jari-jari negatif (harus error)
        with self.assertRaises(ValueError):
            hitung_luas_lingkaran(-1)

if __name__ == '__main__':
    unittest.main()