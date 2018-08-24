from sanic import response, Sanic
app = Sanic(__name__)

@app.route("/", methods=["POST"])
async def root(request):
    data = request.json
    imc = data["mass"] / data["height"] ** 2
    return response.json({"imc": imc})
