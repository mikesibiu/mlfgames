import http.server
import os

os.chdir(os.path.join(os.path.dirname(__file__), 'ticketgame'))
port = int(os.environ.get('PORT', 8000))
httpd = http.server.HTTPServer(('', port), http.server.SimpleHTTPRequestHandler)
print(f'Serving ticketgame on port {port}')
httpd.serve_forever()
