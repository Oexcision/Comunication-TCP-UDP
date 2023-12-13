import socket

# Configurar el cliente UDP
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar datos al servidor UDP
udp_client.sendto("Hola desde el cliente UDP".encode('utf-8'), ("localhost", 9999))

# Recibir la respuesta del servidor UDP
response, addr = udp_client.recvfrom(1024)
print(f"Respuesta UDP: {response.decode('utf-8')} desde {addr}")

# Cerrar la conexión UDP
udp_client.close()
