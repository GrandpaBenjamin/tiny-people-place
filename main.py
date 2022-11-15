import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer, HTTPServer
import time
from tiny_people_sim.World import *

hostName = "localhost"
serverPort = 8080


class Frontend(BaseHTTPRequestHandler):
    def do_GET(self):
        baseGETaddresses = ["/","/api","/"]
        status = 200 if self.path in baseGETaddresses else 404
        for address in baseGETaddresses:
            if address != "/" and self.path.startswith(address):
                status = 200
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == "/":
            self.wfile.write(bytes(f"<html><head><title>TPP - {self.path}</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<h2>TINY PEOPLE PLACE</h2>", "utf-8"))
            self.wfile.write(bytes("<p>hallo. you seem lost<br>Try one of these:</p><p>/api<br>/status<br>/info</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


        if status == 404:
            self.wfile.write(bytes(f"<html><head><title>TPP - {self.path}</title></head>", "utf-8"))
            #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>404 not found</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


def createJSONdata():
    pass

def readDataFromJSON():
    pass


if __name__ == "__main__":
    world = World("hello")
    world.test()
    webServer = ThreadingHTTPServer((hostName, serverPort), Frontend)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    