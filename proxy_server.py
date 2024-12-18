import socket

def start_proxy_server(host, port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Proxy server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_client(client_socket)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Request received: {request}")

    # Assuming request format is: METHOD URL HTTP/1.1
    request_lines = request.split(b'\n')
    url = request_lines[0].split()[1]

    # Parse the URL to extract the host and port
    http_pos = url.find(b'://')
    if http_pos == -1:
        temp = url
    else:
        temp = url[(http_pos+3):]

    port_pos = temp.find(b':')

    # Find end of web server
    webserver_pos = temp.find(b'/')
    if webserver_pos == -1:
        webserver_pos = len(temp)

    webserver = ""
    port = -1
    if (port_pos == -1 or webserver_pos < port_pos):
        port = 80
        webserver = temp[:webserver_pos]
    else:
        port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
        webserver = temp[:port_pos]

    proxy_server(webserver, port, client_socket, request)

def proxy_server(webserver, port, client_socket, request):
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.connect((webserver, port))
    proxy_socket.send(request)

    while True:
        response = proxy_socket.recv(4096)
        if len(response) > 0:
            client_socket.send(response)
        else:
            break

    proxy_socket.close()
    client_socket.close()

if __name__ == "__main__":
    start_proxy_server('127.0.0.1', 8000)