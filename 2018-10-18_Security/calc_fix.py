from flask import Flask, jsonify, abort
app = Flask(__name__)

@app.route("/somar/<a>/<b>")
def somar(a, b):
    try:
        return jsonify({"result": float(a) + float(b)})
    except TypeError:
        abort(404)
