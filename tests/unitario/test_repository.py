import unittest
from api.repository.repository import search_operadoras

class TestRepository(unittest.TestCase):



    def test_search_operadoras_existente(self):
        resultado = search_operadoras("Unimed")
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)  







    def test_search_operadoras_inexistente(self):
        resultado = search_operadoras("Nome Fantasma")
        self.assertIsInstance(resultado, list)
        self.assertEqual(len(resultado), 0)  

if __name__ == "__main__":
    unittest.main()
