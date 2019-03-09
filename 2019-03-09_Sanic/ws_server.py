import asyncio
from sanic import Sanic

app = Sanic(__name__)
app.static("/", "ws_client.html")
connections = set()

async def broadcast(msg):
    print(msg)
    for ws in connections:
        await ws.send(msg)

@app.websocket("/ws")
async def websocket_route(request, ws):
    name = None
    connections.add(ws)
    try:
        name = await ws.recv()
        await broadcast(f"New user: {name}")
        while True:
            message = await ws.recv()
            await broadcast(f"[{name}]: {message}")
    finally:
        connections.remove(ws)
        if name is not None:
            await broadcast(f"{name} left the chat")
