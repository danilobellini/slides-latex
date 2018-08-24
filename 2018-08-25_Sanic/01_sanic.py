from sanic import response, Sanic
app = Sanic(__name__)

@app.route("/")
async def root(request):
    return response.text("Async!")
