import socket
import ssl

# Client (computer 2)
server_ip = computer1_ip
server_port = 8000

# Generate self-signed SSL/TLS certificate (for testing purposes)
certfile = 'client.pem'
keyfile = 'client.key'
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_cert_chain(certfile, keyfile)

# Create a regular socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL/TLS encryption
ssl_client_socket = context.wrap_socket(client_socket, server_hostname=server_ip)

ssl_client_socket.connect((server_ip, server_port))

print(f"Connected to server at {server_ip}:{server_port}")

# Send/receive encrypted data with the server
while True:
    message = input("Enter a message to send: ")
    ssl_client_socket.send(message.encode())

    response = ssl_client_socket.recv(1024).decode()
    print(f"Received response from server: {response}")

    if message.lower() == "exit":
        break

# Close the SSL/TLS connection
ssl_client_socket.close()
