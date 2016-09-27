# A simple localhost server
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

if sys.argv[1:]:
	port = int(sys.argv[1])
else:
	port = 8000
server_address = ("127.0.0.1", port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

socket_access = httpd.socket.getsockname()
print("Serving HTTP on " + str(socket_access[0]) + " port " + str(socket_access[1]) + "...")
httpd.serve_forever()