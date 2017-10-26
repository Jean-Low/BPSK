# Exemplo socket server 
## https://pymotw.com/2/socket/tcp.html

import socket
import sys

class SocketClient:
    def __init__(self):
        self.porta = 1250


    def start_socket(self):
        print("Inicializando socket TCP/IP")
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the port
        server_address = ('localhost', self.porta)
        print("PORTA {}".format(self.porta))
        sock.connect(server_address)

        try:
            # Send data
            message = b'um um pato pato na na lagoa lagoa caiu caiu e e fez fez tibum tibum'
            print("Sending message")
            sock.sendall(message)
            print("Done")

            amount_received = 0
            amount_expected = len(message)
            
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print('received {}'.format(data))

        finally:
            # Clean up the connection
            print('closing socket')
            sock.close()

if __name__ == "__main__":
    SocketClient().start_socket()
