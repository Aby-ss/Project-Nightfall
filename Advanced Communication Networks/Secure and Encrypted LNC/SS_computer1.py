import socket
import ssl

# Server (computer 1)
server_ip = computer1_ip
server_port = 8000

# Generate self-signed SSL/TLS certificate (for testing purposes)
certfile = 'server.pem'
keyfile = 'server.key'
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile, keyfile)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Server listening on {server_ip}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address[0]}:{client_address[1]}")

    # Wrap the socket with SSL/TLS encryption
    ssl_client_socket = context.wrap_socket(client_socket, server_side=True)

    # Handle client requests and send/receive encrypted data
    while True:
        data = ssl_client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received message from client: {data}")

        # Send a response to the client
        response = "This is the server's response."
        ssl_client_socket.send(response.encode())

    # Close the SSL/TLS connection
    ssl_client_socket.close()
