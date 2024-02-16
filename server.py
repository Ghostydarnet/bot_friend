import os 
def server():
    os.system("python3 -m http.server 8080 ")
    server()