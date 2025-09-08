from flask import Flask, jsonify, render_template, make_response
import utils as ut

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def return_all():
    users = ut.return_users()
    return make_response(jsonify(users))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5700)