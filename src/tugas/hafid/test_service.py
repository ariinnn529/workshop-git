import unittest
from service import hitungLuas

class TestService(unittest.TestCase):
    def test_hitung_luas_positive(self):
        self.assertEqual(hitungLuas(5, 4), 20)
        
    def test_hitung_luas_zero(self):
        self.assertEqual(hitungLuas(0, 5), 0)
        self.assertEqual(hitungLuas(5, 0), 0)
        self.assertEqual(hitungLuas(0, 0), 0)

    def test_hitung_luas_negative(self):
        self.assertEqual(hitungLuas(-5, 4), -20)
        self.assertEqual(hitungLuas(-5, -4), 20)

if __name__ == '__main__':
    unittest.main()
