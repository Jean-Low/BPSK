# Exemplo socket server 
## https://pymotw.com/2/socket/tcp.html

import npyscreen as ns 
import socket
import sys


class FormObj( ns.Form ):
	
	msgWidget = None
	
	def create (self):
		FormObj.msgWidget = self.add( ns.TitleText,name = "MESSAGE:", value = "  <<< PRESS OK TO CONTINUE >>>  ", editable = False)
		#self.parentApp.setNextForm( "2" )
	
	def afterEditing ( self ):
		self.parentApp.switchForm( MsgObj )
		pass
		
		
class MsgObj( ns.Form ):
	
	rcvWidget = None
	
	def create (self):
		MsgObj.rcvWidget = self.add( ns.TitleText,name = "Receiving", value = "<<< WAITING  >>>", editable = False)
	
	def afterEditing ( self ):
		self.parentApp.setNextForm( None )
		#SocketServer(1234).start_socket()
		pass

class App( ns.NPSAppManaged):
	
	def onStart( self):
		self.addForm("2",FormObj, name = "Super Chat! The best chat with no noise... almost. < WAITING >")
		self.addForm("MAIN",FormObj, name = "Super Chat! The best chat with no noise... almost. < RECEIVING >")					


class SocketServer:
    def __init__(self,port):
        self.porta = port

    def start_socket(self):
        #print("Server: receber dados")
        #print("Inicializando socket TCP/IP")
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the port
        server_address = ('localhost', self.porta)
        #print("PORTA {}".format(self.porta))
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)

        while True:
            # Wait for a connection
            #print("waiting for a connection")
            connection, client_address = sock.accept()

            try:
                #print(" connection from {}".format(client_address))
                
                FormObj.msgWidget.value = "  --->  "
                
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(16)
                    # print("{}".format(data))
                    FormObj.msgWidget.value += ("{}".format(data))
                    if(len(data) <= 0):
                        break

            finally:
                # Clean up the connection
                connection.close()


if ( __name__ == "__main__"):
     app = App().run()
     SocketServer(1234).start_socket()


#if __name__ == "__main__":
#    SocketServer().start_socket()
