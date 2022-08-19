from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/connect")
def connect():
    return "Connected!"


@app.route("/move")
def move_xyz():

    x = request.args.get("x")
    y = request.args.get("y")
    z = request.args.get("z")
    return f"Me moví a (x, y, x): ({x}, {y}, {z})"


if __name__ == "__main__":
    app.run(debug=True)
