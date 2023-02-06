from flask import Flask, request, jsonify
from server import util


app = Flask(__name__)


# @app.route decorator exposes the http enedpoint
@app.route("/hello")
def test():
    return "hello world"


@app.route("/get-locations")
def get_locations():
    response = jsonify(
        {
            "locations": util.get_locations()
        }
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print("python flask server started...")
    app.run()