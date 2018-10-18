from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/somar/<a>/<b>")
def somar(a, b):
    return jsonify({"result": eval(a) + eval(b)})
