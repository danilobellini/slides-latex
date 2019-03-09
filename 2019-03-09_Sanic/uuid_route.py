from sanic import Sanic, response

app = Sanic(__name__)

@app.route("/<uid:uuid>")
def root(request, uid):
    return response.json({"user": uid.hex})
