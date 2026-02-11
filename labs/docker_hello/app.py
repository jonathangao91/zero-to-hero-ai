from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello from the refreshed MOUNTED World!')


print("Server starting on port 8080")
HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
