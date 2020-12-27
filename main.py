from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import os

COMMAND = input("COMMAND: ")

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        os.system(COMMAND)


httpd = HTTPServer(("", 8000), RequestHandler)
httpd.serve_forever()
