from http.server import HTTPServer, BaseHTTPRequestHandler
import codecs, time


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = codecs.open(self.path[1:], "r", "UTF-8").read()
            self.send_response(200)
            try:
                self.end_headers()
                self.wfile.write(bytes(file_to_open, "UTF-8"))
            except AttributeError:
                pass
        except UnicodeDecodeError:
            pass
        except UnboundLocalError:
            pass
        except:
            file_to_open = "File not found"
            self.send_response(404)
def siteFunc():
    host = "192.168.0.106"
    print("---------------------------INSTRUCTIONS---------------------------\n" +
    "How to find out ipv4? - Open a command line \nand then write ipconfig then look for the ipv4 entry of your network!\n" +
    "The server does not start! Open port 55555 on your router! \nGoogle how to do it!\n" +
    "Then this application will do everything for you!\nProvided that you download all the necessary libraries!\n" +
    "---------------------------INSTRUCTIONS---------------------------\n")
    host = input("ВВЕДИТЕ IPv4 АДРЕС КОМПЬЮТЕРА:")
    httpd = HTTPServer((host, 55555), Server)
    print("" +
    "  ____  _____ ______     _______ ____    ____ _____  _    ____ _____ _____ ____   \n" +
    " / ___|| ____|  _ \ \   / / ____|  _ \  / ___|_   _|/ \  |  _ \_   _| ____|  _ \  \n" +
    " \___ \|  _| | |_) \ \ / /|  _| | |_) | \___ \ | | / _ \ | |_) || | |  _| | | | | \n" +
    "  ___) | |___|  _ < \ V / | |___|  _ <   ___) || |/ ___ \|  _ < | | | |___| |_| | \n" +
    " |____/|_____|_| \_\ \_/  |_____|_| \_\ |____/ |_/_/   \_\_| \_\|_| |_____|____/  \n" +
    "\n" +
    "         PYTHON HTTP HOSTING SERVER  >>>  by srgwrtg0342"
    )

    print(f"Http server on - http://{host}:55555/index.html (url without spaces)")
    httpd.serve_forever()

siteFunc()
