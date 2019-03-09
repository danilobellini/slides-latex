#!/usr/bin/env python3
import socket, sys, os
from sanic import Sanic, response

app = Sanic(__name__)
server_socket = "/tmp/sanic.sock"
sock = socket.socket(socket.AF_UNIX,
                     socket.SOCK_STREAM)
sock.bind(server_socket)
app.count = 0

@app.route("/")
async def counter(request):
    app.count += 1
    return response.text(app.count)

def signal_handler(sig, frame):
    print("Exiting")
    os.unlink(server_socket)
    sys.exit(0)

if __name__ == "__main__":
    app.run(sock=sock)
