from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from tiny_people_sim.World import *

HOST = "localHOST"
PORT = 8080

class Frontend(BaseHTTPRequestHandler):

    def sendHeaders(self,status,type):
        self.send_response(status)
        self.send_header("Content-type", type)
        self.end_headers()

    def do_GET(self):
        baseGETaddresses = ["/","/api","/save","/json","status","/info"]
        status = 200 if self.path in baseGETaddresses else 404
        for address in baseGETaddresses:
            if address != "/" and self.path.startswith(address):
                status = 200
        if self.path == "/":
            self.sendHeaders(status,"text/html")
            self.wfile.write(bytes(f"<html><head><title>TPP - {self.path}</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<h2>TINY PEOPLE PLACE</h2>", "utf-8"))
            self.wfile.write(bytes("<p>hallo. you seem lost<br>Try one of these:</p><p><b>/api</b><br><b>/status</b><br><b>/info</b><br><b>/save</b> or <b>/json</b><br>or maybe even <b>/docs</b></p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif self.path == "/save" or self.path == "/json":
            self.sendHeaders(status,"application/json")
            self.wfile.write(bytes(open("./saves/save.json").read(),"utf-8"))

        if status == 404:
            self.sendHeaders(status,"text/html")
            self.wfile.write(bytes(f"<html><head><title>TPP - {self.path}</title></head>", "utf-8"))
            #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>404 not found</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    world = World("./saves/save.json", "./worldSettings.json")
    webServer = ThreadingHTTPServer((HOST, PORT), Frontend)
    print("Server started http://%s:%s" % (HOST, PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    