from flask import jsonify, request, Flask
app = Flask(__name__)

@app.route("/", methods=["POST"])
def root():
    data = request.get_json()
    imc = data["mass"] / data["height"] ** 2
    return jsonify({"imc": imc})
