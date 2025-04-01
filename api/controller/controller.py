import http.server
import urllib.parse
import json
from service.service import search_operadoras_service
from datetime import date, datetime

class OperadoraController(http.server.BaseHTTPRequestHandler):

#Função para tratar requisições GET
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        if parsed_path.path == "/search":
            query_params = urllib.parse.parse_qs(parsed_path.query)
            query = query_params.get("query", [""])[0]
            
            if not query:
                self._send_response(400, {"error": "A query é obrigatória"})
                return

            operadoras = search_operadoras_service(query)
            self._send_response(200, operadoras)
        else:
            self.send_response(404)
            self.end_headers()







#Função para enviar a resposta JSON
    def _send_response(self, status_code, response_data):
        """Envia uma resposta JSON padronizada, convertendo datas para string."""
        def json_serial(obj):
            """Função auxiliar para serializar objetos datetime e date."""
            if isinstance(obj, (datetime, date)):
                return obj.isoformat()  
            raise TypeError(f"Tipo {type(obj)} não é serializável em JSON")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data, default=json_serial).encode("utf-8"))
