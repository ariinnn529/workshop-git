import unittest
import importlib.util
import os

# Helper untuk mengimpor module dengan nama folder yang mengandung hyphen (-)
def import_service():
    module_name = "service"
    # Menentukan path absolut ke service.py
    # Struktur: src/tugas/Fatwabith-akbar/service.py
    current_dir = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(current_dir, "../../../src/tugas/Fatwabith-akbar/service.py"))
    
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    service = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(service)
    return service

service = import_service()

class TestService(unittest.TestCase):
    def test_hitung_luas_positif(self):
        # Test dengan nilai positif
        self.assertEqual(service.hitung_luas(10, 5), 50)
        self.assertEqual(service.hitung_luas(20, 10), 200)

    def test_hitung_luas_nol(self):
        # Test dengan nilai nol
        self.assertEqual(service.hitung_luas(0, 5), 0)
        self.assertEqual(service.hitung_luas(10, 0), 0)

    def test_hitung_luas_desimal(self):
        # Test dengan nilai desimal
        self.assertEqual(service.hitung_luas(5.5, 2), 11.0)

if __name__ == "__main__":
    unittest.main()
