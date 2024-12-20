import http.server
import socketserver
PORT = 8000
class TestMe():
"""Класс для тестирования функциональности сервера."""
    def take_five(self):
        """Возвращает число 4."""
        return 4
    def port(self):
        """Возвращает номер порта."""
        return PORT
if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
