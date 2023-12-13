import socket

# Configurar el cliente TCP
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(("localhost", 8888))

# Enviar datos al servidor TCP
tcp_client.send("Hola desde el cliente TCP".encode('utf-8'))

# Recibir la respuesta del servidor TCP
response = tcp_client.recv(1024)
print(f"Respuesta TCP: {response.decode('utf-8')}")

# Cerrar la conexión TCP
tcp_client.close()
