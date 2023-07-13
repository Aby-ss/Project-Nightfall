import socket
import threading
from rich import box
from rich.panel import Panel

from rich.traceback import install
install(show_locals=True)

# Server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

# List to store connected clients
clients = []

# Flag to control server loop
running = True

def handle_client(client_socket, client_address):
    while running:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')

            # Check if server is being closed
            if message == 'q':
                print(Panel('Server is shutting down...', border_style="bold red", box=box.SQUARE))
                running = False
                break

            # Broadcast the message to all connected clients
            for client in clients:
                if client != client_socket:
                    client.send(f'{client_address[0]}: {message}'.encode('utf-8'))
        except:
            # Client has disconnected
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(Panel('Server started. Waiting for connections...', border_style="bold green", box=box.SQUARE))

    while running:
        # Accept client connection
        client_socket, client_address = server_socket.accept()

        # Add client to the list
        clients.append(client_socket)

        # Start a new thread to handle client communication
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

    # Close all client connections
    for client_socket in clients:
        client_socket.close()

    # Close the server socket
    server_socket.close()

if __name__ == '__main__':
    start_server()
