import unittest
from service import hitungluas


class TestHitungLuas(unittest.TestCase):

    def test_luas_normal(self):
        self.assertEqual(hitungluas(10, 5), 50)

    def test_luas_desimal(self):
        self.assertEqual(hitungluas(2.5, 4), 10)

    def test_luas_nol(self):
        self.assertEqual(hitungluas(0, 5), 0)


if __name__ == "__main__":
    unittest.main()