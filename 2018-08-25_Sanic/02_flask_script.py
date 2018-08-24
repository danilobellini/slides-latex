from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "Sync!"

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port="1337",
        debug=True,
    )
