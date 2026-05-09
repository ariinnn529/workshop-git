import unittest
from src.tugas.ajiputraprayogi.service import hitung_luas

class TestService(unittest.TestCase):
    def test_hitung_luas(self):
        # Menguji perhitungan luas dengan angka positif
        self.assertEqual(hitung_luas(5, 4), 20)
        
        # Menguji perhitungan luas dengan nol
        self.assertEqual(hitung_luas(0, 10), 0)
        self.assertEqual(hitung_luas(5, 0), 0)
        
        # Menguji perhitungan luas dengan bilangan desimal (float)
        self.assertEqual(hitung_luas(2.5, 4), 10.0)

if __name__ == '__main__':
    unittest.main()
