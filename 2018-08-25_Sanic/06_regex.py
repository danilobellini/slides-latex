from sanic import response, Sanic
app = Sanic(__name__)

@app.route("/imc/<mass:\d+(?:.\d+)?>/<height:\d+(?:.\d+)?>")
async def imc(request, mass, height):
    try:
        imc = float(mass) / float(height) ** 2
    except (ValueError, TypeError):
        return response.json({"error": "bad_request"},
                             status=400)
    return response.json({"imc": imc})
