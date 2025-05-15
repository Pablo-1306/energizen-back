from flask import (
    Flask,
    jsonify,
    make_response,
    request
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from controller.user import (validate_user, create_user)


@app.route("/", methods=["POST","GET"])
def root():
    if request.method == "POST":
        return jsonify(message = "ACTIVE")
    if request.method == "GET":
        return jsonify(message = "ACTIVE")


@app.route("/user/validate", methods=["POST"])
def validate_user_():
    if request.method == "POST":
        return validate_user(request)

@app.route("/user/create", methods=["POST"])
def create_user_():
    if request.method == "POST":
        return create_user(request)

    
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if __name__ == '__main__':
    try:
        app.run(debug=True, host="0.0.0.0", port=5050)
    except Exception as e:
        print(e)
