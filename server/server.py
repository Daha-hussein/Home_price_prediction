from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    area = float(data['area'])
    bedrooms = int(data['bedrooms'])
    bathrooms = int(data['bathrooms'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(area, bedroooms, bathrooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    # Change the port number to your desired value
    app.run(port=8040)