import socketserver
from controller.controller import OperadoraController

PORT = 5000

with socketserver.TCPServer(("0.0.0.0", PORT), OperadoraController) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    httpd.serve_forever()
