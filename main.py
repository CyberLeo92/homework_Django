# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Настройки запуска
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        # На ЛЮБОЙ GET-запрос возвращаем страницу "Контакты"
        try:
            # Читаем HTML-файл через with open()
            with open("contacts.html", "r", encoding="utf-8") as file:
                html_content = file.read()

            # Отправляем успешный ответ
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Отправляем HTML-содержимое
            self.wfile.write(bytes(html_content, "utf-8"))

        except FileNotFoundError:
            # Если файл не найден
            self.send_error(404, "File contacts.html not found")
        except Exception as e:
            # Обработка других ошибок
            self.send_error(500, f"Server error: {str(e)}")


if __name__ == "__main__":
    # Создаем экземпляр веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")
    print("Any GET request will return contacts.html page")

    try:
        # Запускаем сервер
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")

    # Корректно останавливаем сервер
    webServer.server_close()
    print("Server stopped.")