import socket
ip = socket.gethostbyname(socket.gethostname())
print (ip)
with open("httpy.sh","w") as f:
    f.write("python3 -m http.server 8000 --cgi --bind "+ip+"\n")
