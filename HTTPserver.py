#HTTP Server v Pythone
#Pre Teplomer


import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


Handler = SimpleHTTPRequestHandler
Server  = BaseHTTPServer.HTTPServer
Protokol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8080
server_address = ('127.0.0.1', port)

Handler.protocol_version = Protokol
httpd = Server(server_address, Handler)

sa = httpd.socket.getsockname()
print ("Serving HTTP on", sa[0], "port", sa[1], "...")
httpd.serve_forever()
