import socket

# Create a TCP/IP Socket
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = "localhost"
port = 65432

# Connect the socket to the port where the server is listening
server_address = ((host, port))
print("Connecting")

stream_socket.connect(server_address)

# Send data
message = "Hello world"
stream_socket.sendall(message.encode())

# Response
data = stream_socket.recv(10)
print(message)

#stream_socket.close()

