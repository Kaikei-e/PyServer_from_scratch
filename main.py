import socket

ServerHost = '0.0.0.0'
ServerPort = 9020

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((ServerHost, ServerPort))
serverSocket.listen(1)

print('Listening on port %s ...' % ServerPort)

while True:
    clientConnection, clientAddress = serverSocket.accept()

    request = clientConnection.recv(1024).decode()
    print(request)

    response = 'HTTP/1.0 200 OK\n\nHello World'
    clientConnection.sendall(response.encode())
    clientConnection.close()


serverSocket.close()
