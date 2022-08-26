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


@app.route("/set_joints")
def set_joints():

    q0 = request.args.get("q0")
    q1 = request.args.get("q1")
    q2 = request.args.get("q2")

    return f"Mi nueva pose es: (q0={q0}, q1={q1}, q2={q2})"


if __name__ == "__main__":
    app.run(debug=False)
