import http.server
import socketserver
import os
os.chdir(r"E:\invate  story\works\Bhava-weds-Sanyam")
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()
