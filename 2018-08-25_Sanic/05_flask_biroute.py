from flask import jsonify, request, Flask
app = Flask(__name__)

@app.route("/imc", methods=["POST"])
@app.route("/imc/<float:mass>/<float:height>")
def imc(mass=None, height=None):
    try:
        if request.method == "POST":
            data = request.get_json()
            mass = data["mass"]
            height = data["height"]
        imc = mass / height ** 2
    except (ValueError, KeyError, TypeError):
        return jsonify({"error": "bad_request"}), 400
    return jsonify({"imc": imc})
