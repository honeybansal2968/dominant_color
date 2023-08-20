from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from flask_cors import CORS
from collections import Counter
import requests

app = Flask(__name__)
CORS(app)
@app.route('/get_dominant_color', methods=['POST'])
def get_dominant_color():
    data = request.json
    image_url = data.get('image_url')

    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        pixel_data = list(image.getdata())
        color_count = Counter(pixel_data)
        
        dominant_color = color_count.most_common(1)[0][0]
        print(dominant_color)
        return jsonify({"dominant_color": dominant_color})
    else:
        return jsonify({"error": "Image not found or couldn't be fetched."}), 404

if __name__ == '__main__':
    app.run(debug=True)
