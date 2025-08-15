from flask import Flask, make_response, jsonify, render_template

app = Flask(__name__)

@app.route("/all", methods=["GET"])
def return_all():
    return make_response(jsonify({"Nome": "Gabriel"}))


if __name__ == "__main__":
    app.run(host="localhost", port=5500)