import unittest
from api.service.service import search_operadoras_service

class TestService(unittest.TestCase):




    
    def test_service_operadoras(self):
        resultado = search_operadoras_service("Unimed")
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

if __name__ == "__main__":
    unittest.main()
