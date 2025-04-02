
import http.server
import urllib.parse
import json
from service.service import search_operadoras_service
from datetime import date, datetime

class OperadoraController(http.server.BaseHTTPRequestHandler):



    # Função para tratar requisições GET
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)

        if parsed_path.path == "/search":
            query_params = urllib.parse.parse_qs(parsed_path.query)
            query = query_params.get("query", [""])[0]

            if not query:
                self._send_cors_response(400, {"error": "A query é obrigatória"})
                return

            operadoras = search_operadoras_service(query)
            self._send_cors_response(200, operadoras)
        else:
            self.send_response(404)
            self.end_headers()






    # Função para enviar resposta CORS
    def _send_cors_response(self, status_code, response_data):
 
        def json_serial(obj):
  
            if isinstance(obj, (datetime, date)):
                return obj.isoformat()
            raise TypeError(f"Tipo {type(obj)} não é serializável em JSON")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Aqui configurei para aceitar de qualquer origem
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(json.dumps(response_data, default=json_serial).encode("utf-8"))







    # Função para permitir OPTIONS 
    def do_OPTIONS(self):
        """Responde às requisições OPTIONS para suporte a CORS."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
