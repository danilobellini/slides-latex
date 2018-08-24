from sanic import response, Sanic
app = Sanic(__name__)

@app.route("/", methods=["POST"])              # Sanic
async def root(request):
    data = request.json
    try:
        imc = data["mass"] / data["height"] ** 2
    except (ValueError, KeyError, TypeError):
        return response.json({"error": "bad_request"},
                             status=400)
    return response.json({"imc": imc})
