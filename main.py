import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import time

hostName = "localhost"
serverPort = 8080


class Frontend(BaseHTTPRequestHandler):
    def do_GET(self):
        status = 404
        
        if self.path == "/":
            self.send_response("harro")


        if status == 404:
            self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
            #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>404 not found</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()


def createJSONdata():
    pass

def readDataFromJSON():
    pass


if __name__ == "__main__":        
    webServer = ThreadingHTTPServer((hostName, serverPort), Frontend)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")