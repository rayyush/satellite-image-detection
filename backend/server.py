from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from PIL import Image as PILImage
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    image = PILImage.open(image_file)
    
    # Perform your image processing here
    # For example: Convert to grayscale
    processed_image = image.convert('L')

    # Save processed image to a BytesIO object
    img_byte_arr = io.BytesIO()
    processed_image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)

    # Return the processed image
    return send_file(img_byte_arr, mimetype='image/jpeg', as_attachment=True, download_name='processed_image.jpg')

if __name__ == '__main__':
    app.run(debug=True)
