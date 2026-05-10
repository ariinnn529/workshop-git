import unittest

from src.Tugas.Muhammad_Destha_Prastyo.service import luas

class TestLuad(unittest.TestCase):
    def LuasTaman(self):
        hasil = luas(5, 5)
        self.assertEqual(hasil, 25)