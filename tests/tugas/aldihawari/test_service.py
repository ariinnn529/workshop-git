import unittest
from src.tugas.aldihawari.service import luas

class TestServices(unittest.TestCase):
    def test_luas_positif(self):
        self.assertEqual(luas(10, 20), 200)

    def test_luas_negatif(self):
        self.assertEqual(luas(-20, -20), 400)

    def test_luas_nol(self):
        self.assertEqual(luas(5, 0), 0)
        self.assertEqual(luas(0, 2), 0)
        self.assertEqual(luas(0, 0), 0)

    if __name__ == '__main__':
        unittest.main()
