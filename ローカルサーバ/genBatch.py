import socket
ip = socket.gethostbyname(socket.gethostname())
print (ip)
with open("WebSrv.bat","w") as f:
    f.write("python -m http.server 8000 --cgi --bind "+ip+"\n")
