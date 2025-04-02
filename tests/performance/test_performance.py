from locust import HttpUser, task

class TestAPI(HttpUser):


    
    @task
    def test_busca_operadora(self):
        self.client.get("/buscar-operadoras?query=Unimed")

