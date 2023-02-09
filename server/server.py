from flask import Flask, request, jsonify
import util


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

@app.route("/predict-price", methods=['POST'])
def predict_price():
    loc = request.form["loc"]
    sqft = float(request.form["sft"])
    bedrooms = int(request.form["bedrooms"])
    bath = int(request.form["bath"])

    response = jsonify(
        {
            "approximate_price": util.get_approx_price(loc, sqft, bedrooms, bath)
        }
    )
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    print("python flask server started...")
    util.load_artifacts()
    app.run()