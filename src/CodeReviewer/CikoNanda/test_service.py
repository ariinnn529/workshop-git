import unittest
from service import hitung_luas_jajargenjang


class TestJajarGenjang(unittest.TestCase):

    def test_luas_normal(self):
        self.assertEqual(
            hitung_luas_jajargenjang(10, 5),50)

    def test_luas_nol(self):
        self.assertEqual(
            hitung_luas_jajargenjang(0, 5),0)

    def test_luas_negatif(self):
        self.assertEqual(
            hitung_luas_jajargenjang(-2, 5),-10)


if __name__ == "__main__":
    unittest.main()