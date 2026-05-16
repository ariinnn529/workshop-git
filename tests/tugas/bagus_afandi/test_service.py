import unittest
from src.tugas.bagus_afandi.service import persegi_panjang

class TestPersegiPanjang(unittest.TestCase):
    def test_persegi_panjang(self):
        self.assertEqual(persegi_panjang(5, 3), 15)