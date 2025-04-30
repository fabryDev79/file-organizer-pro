# QUICKSCAN WEB
# by @Fabry79
# Scanner basilare per header di sicurezza HTTP e info SSL

print("""
  ____        _      _      ____                      
 |  _ \ _   _| | ___| |__  / ___| _ __   ___  ___ ___ 
 | |_) | | | | |/ __| '_ \ \___ \| '_ \ / _ \/ __/ __|
 |  __/| |_| | | (__| | | | ___) | |_) |  __/\__ \__ \\
 |_|    \__,_|_|\___|_| |_| |____/| .__/ \___||___/___/
                                 |_|                  
             QUICKSCAN WEB  -  by @Fabry79
""")

import requests
import ssl
import socket
from urllib.parse import urlparse

# Funzione: controlla header HTTP
def check_headers(url):
    try:
        response = requests.get(url)
        print("\n[HTTP HEADERS CHECK]")
        security_headers = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy"
        ]
        for header in security_headers:
            if header in response.headers:
                print(f"[OK] {header}: {response.headers[header]}")
            else:
                print(f"[WARN] {header} non trovato.")
    except Exception as e:
        print(f"[ERRORE] Durante la richiesta: {e}")

# Funzione: info certificato SSL
def check_ssl_info(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        port = 443

        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print("\n[SSL CERTIFICATE INFO]")
                print(f"[INFO] Emesso da: {cert['issuer'][-1][1]}")
                print(f"[INFO] Valido da: {cert['notBefore']}")
                print(f"[INFO] Valido fino a: {cert['notAfter']}")
    except Exception as e:
        print(f"[ERRORE] SSL non verificabile: {e}")

# Main
if __name__ == "__main__":
    target = input("Inserisci l'URL da scansionare (es. https://example.com): ").strip()
    if not target.startswith("http"):
        target = "https://" + target

    check_headers(target)
    check_ssl_info(target)
