import socket
# HTTP: using tcp, ip
# ip-address: 5000 - socket
# 
# tcp - transfer controll protocol

URLS = {
    '/': 'hello index',
    '/blog': 'hello blog'
}

def parse_request(request):
    parsed = request.split(' ')
    # print(parsed)
    method = parsed[0]
    url = parsed[1]
    # print(method, url)
    return (method, url)

def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 METHOD not allowed\n\n', 405)
    
    if not url in URLS:
        return ('HTTP/1.1 404 Page not found\n\n', 404)
    
    return ('HTTP/1.1 200 OK\n\n', 200)

def generate_content(code, url):
    if code == 404:
        return '<h1> 404 </h1> <p> Not found </p>'
    if code == 405:
        return "<h1> 405 </h1> <p> Method not allowed </p>"
    return f"<h1>{URLS[url]}<h2>"

def generate_response(request):
    method, url = parse_request(request) 
    headers, code = generate_headers(method, url)
    print(code)
    print(headers)
    body = generate_content(code, url)

    return (headers + body).encode()

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)
        print('\n',addr)

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()



if __name__ == '__main__':
    run()
