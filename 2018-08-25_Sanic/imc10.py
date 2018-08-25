from sanic import response, Blueprint
bp = Blueprint(__name__)

@bp.route("/imc")
async def imc(request):
    try:
        mass = request.args["mass"][0]
        height = request.args["height"][0]
        imc = float(mass) / float(height) ** 2
    except (ValueError, KeyError, TypeError):
        return response.json({"error": "bad_request"},
                             status=400)
    return response.json({"imc": imc})
