import npyscreen as ns 
import socket
import sys


#class valueManager( ns.TitleText):
	
#	def __init__(self,*args, **keywords):
		
#		super(valueManager,self).__init__(*args, **keywords)
	
#	def when_value_edited(self):
#		self.parent.port = 9

class SocketClient:
    def __init__(self,porta):
        self.porta = 1250


    def start_socket(self, message):
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
            #message = b'um um pato pato na na lagoa lagoa caiu caiu e e fez fez tibum tibum'
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


class FormObj( ns.Form ):
	
	portWidget = None
	msgWidget = None
	
	def create (self):
		FormObj.portWidget = self.add( ns.TitleText,name = "Port", value = "1250", editable = True)
		FormObj.msgWidget = self.add( ns.TitleText,name = "Message", value = "", editable = True)
		#self.add(valueManager, name = "set Port")
		
	def afterEditing ( self ):
		self.parentApp.setNextForm( None )
		#time.sleep(3) #proof that it worked
		client = SocketClient(int(FormObj.portWidget.value))
		client.start_socket(FormObj.msgWidget.value)

class App( ns.NPSAppManaged):
	
	def onStart( self):
		self.addForm("MAIN",FormObj, name = "Super Chat! The best chat with no noise... almost.")	
		
			

if ( __name__ == "__main__"):
     app = App().run()
     print("OOP is the bestframework")
     



#if __name__ == "__main__":
#    SocketClient().start_socket()
