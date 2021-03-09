import socket
import json


# Хост и порт, где сервер слушает сообщения
PORT = 45400
HOST = "127.0.0.1"


# Получение заголовков запроса и их преобразование к json
def headers_json(data):
    all_data = data.split('\r\n')
    headers = []
    headers_dict = {}
    for i in all_data:
        if ":" in i:
            headers.append(i)
    for i in headers:
        key, value = i.split(": ")
        headers_dict[key] = value
    json_obj = json.dumps(headers_dict)
    return json_obj

my_socket = socket.socket()
my_socket.bind((HOST, PORT))
print(f"Запуск сокета: {HOST}:{PORT}")

# Команда сокету на прослушивание сообщений
my_socket.listen(1)

# Принимаем подключения
conn, addr = my_socket.accept()

# Получаем и обрабатываем данные
data = conn.recv(1024).decode('utf-8')
print(f"Got data: {data} from {addr}")

# Отправляем ответа клиенту RESPONSE_HEADERS в виде JSON
RESPONSE_HEADERS = "HTTP/1.1 200 OK\r\nContent-Length: 1024\r\nConnection: close\r\nContent-Type: application/json\n\n"
conn.send(f"{RESPONSE_HEADERS} {headers_json(data)}".encode("utf-8"))
conn.close()

