import unittest
import os
import importlib.util

class TestService(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        service_path = os.path.join(base_dir, '..', '..', '..', 'src', 'tugas', 'achmad-chilmi', 'service.py')
        service_path = os.path.abspath(service_path)
        
        spec = importlib.util.spec_from_file_location("service", service_path)
        self.service = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.service)

    def test_hitung_luas_persegi(self):
        
        self.assertEqual(self.service.hitung_luas_persegi(5, 4), 20)
        
        
        self.assertEqual(self.service.hitung_luas_persegi(10, 10), 100)
        
        self.assertEqual(self.service.hitung_luas_persegi(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
