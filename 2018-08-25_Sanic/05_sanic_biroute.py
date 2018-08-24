from sanic import response, Sanic
app = Sanic(__name__)

@app.route("/imc", methods=["POST"])
@app.route("/imc/<mass:number>/<height:number>")
async def imc(request, mass=None, height=None):
    try:
        if request.method == "POST":
            mass = request.json["mass"]
            height = request.json["height"]
        imc = mass / height ** 2
    except (ValueError, KeyError, TypeError):
        return response.json({"error": "bad_request"},
                             status=400)
    return response.json({"imc": imc})
