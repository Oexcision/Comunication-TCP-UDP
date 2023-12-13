import socket
import threading

# Función para manejar la comunicación TCP con un cliente
def handle_tcp_client(client_socket):
    # Recibir datos desde el cliente
    request = client_socket.recv(1024)
    print(f"Recibido TCP: {request.decode('utf-8')}")

    # Enviar una respuesta al cliente
    response = "Hola desde el servidor TCP"
    client_socket.send(response.encode('utf-8'))

    # Cerrar la conexión
    client_socket.close()

# Función para manejar la comunicación UDP
def handle_udp_server():
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind(("0.0.0.0", 9999))

    while True:
        # Recibir datos desde el cliente UDP
        data, addr = udp_server.recvfrom(1024)
        print(f"Recibido UDP: {data.decode('utf-8')} desde {addr}")

        # Enviar una respuesta al cliente UDP
        response = "Hola desde el servidor UDP"
        udp_server.sendto(response.encode('utf-8'), addr)

# Configurar el servidor TCP
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("0.0.0.0", 8888))
tcp_server.listen(5)

# Configurar el hilo para manejar el servidor UDP
udp_thread = threading.Thread(target=handle_udp_server)
udp_thread.start()

print("Servidor encendido y escuchando en TCP en el puerto 8888 y en UDP en el puerto 9999")

while True:
    # Esperar a que un cliente se conecte al servidor TCP
    client, addr = tcp_server.accept()
    print(f"Conexión aceptada desde {addr}")

    # Configurar un hilo para manejar la comunicación con el cliente TCP
    client_handler = threading.Thread(target=handle_tcp_client, args=(client,))
    client_handler.start()
