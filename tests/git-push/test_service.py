import unittest
from src.kelompok1.hafid.service import luasJajarGenjang

class TestLuasJajarGenjang(unittest.TestCase):

    def test_luas_positif(self):
        self.assertEqual(luasJajarGenjang(2, 3), 6)

    def test_luas_nol(self):
        self.assertEqual(luasJajarGenjang(0, 5), 0)

    def test_luas_desimal(self):
        self.assertEqual(luasJajarGenjang(2.5, 4), 10.0)

    def test_luas_negatif(self):
        self.assertEqual(luasJajarGenjang(-2, 3), -6)

if __name__ == "__main__":
    unittest.main()