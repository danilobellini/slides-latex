from sanic import response, Sanic
app = Sanic(__name__)

@app.route("/")
async def root(request):
    return response.text("Async!")

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port="1337",
        debug=True,
        workers=4,
    )
