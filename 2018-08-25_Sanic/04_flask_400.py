from flask import jsonify, request, Flask
app = Flask(__name__)

@app.route("/", methods=["POST"])              # Flask
def root():
    data = request.get_json()
    try:
        imc = data["mass"] / data["height"] ** 2
    except (ValueError, KeyError, TypeError):
        return jsonify({"error": "bad_request"}), 400
    return jsonify({"imc": imc})
