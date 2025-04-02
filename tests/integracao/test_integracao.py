import unittest
from http.server import HTTPServer
import threading
import requests

from api.controller.controller import OperadoraController


class TestController(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("localhost", 8081), OperadoraController)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.setDaemon(True)
        cls.server_thread.start()




    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()






    def test_get_search_operadora(self):
        response = requests.get("http://localhost:8081/search?query=Unimed")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)





    def test_get_search_sem_query(self):
        response = requests.get("http://localhost:8081/search")
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
