from flask import Flask, jsonify, make_response

# == [ APP FACTORY ] == #
def create_app():

    # == [ APP ] == #
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return make_response(jsonify({"message": "Hello Events"}), 200)

    return app