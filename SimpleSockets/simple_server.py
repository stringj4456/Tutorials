import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = "localhost"
port = 65432

# Bind the socket to the port
sock.bind((host, port))

# Listen for an incoming connection
sock.listen(5)

# Wait for a connection
print("Waiting for a connection")
connection, client = sock.accept()

print(client, "Connected")
print()

# Receive data in small chunks and retransmit
data = connection.recv(16)
print("received '%s'" %data)

if data:
    connection.sendall(data)
else:
    print("No data from", client)

# Close the connection
connection.close()
