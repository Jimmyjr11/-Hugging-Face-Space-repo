from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)  # ✅ Corrected
CORS(app)  # Enable CORS for all domains

@app.route('/')
def home():
    return 'Flask API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    image.save('input.jpg')  # Save image temporarily

    # TODO: Replace with actual model prediction logic
    result = ["leaf_blight", "rust"]

    return jsonify({'diseases': result})

if __name__ == '__main__':  # ✅ Corrected
    app.run(host='0.0.0.0', port=7860)
