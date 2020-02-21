import socket, threading

local_host = '127.0.0.1'
local_port = 4444
remote_host = '127.0.0.1'
remote_port = 1337

def transfer(src, dst1, dts2):
    while True:
        data = src.recv(1024)
        if data.decode()[0:2]== '(:'
        dst.send(data)

def server():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((local_host, local_port))
    s.listen(5)
    while True:
        local_socket, local_address = s.accept()
        remote_socket = socket.socket()
        remote_socket.connect((remote_host, remote_port))
        t1 = threading.Thread(target=transfer, args=(remote_socket, local_socket))
        t2 = threading.Thread(target=transfer, args=(local_socket, remote_socket))
        
        t1.start()
        t2.start()

if __name__ == "__main__":
    server()
