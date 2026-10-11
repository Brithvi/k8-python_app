from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import socket

class APIHandler(BaseHTTPRequestHandler):
    def respond(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/healthz":
            self.respond(200, {"status": "healthy"})
        elif self.path == "/api/hello":
            self.respond(200, {
                "message": "Hello from Kubernetes!",
                "hostname": socket.gethostname(),
                "environment": os.getenv("APP_ENV", "dev")
            })
        else:
            self.respond(404, {"error": "Not found"})

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))

server = HTTPServer(("0.0.0.0", 8080), APIHandler)
print("Python API listening on port 8080", flush=True)
server.serve_forever()
