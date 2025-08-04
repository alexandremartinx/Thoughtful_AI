from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import Package

app = Flask(__name__)
CORS(app)

def parse_package_data(data):
    try:
        width = float(data['width'])
        height = float(data['height'])
        length = float(data['length'])
        mass = float(data['mass'])
        if width < 0 or height < 0 or length < 0 or mass < 0:
            return None, "All dimensions and mass must be non-negative."
        pkg = Package(width, height, length, mass)
        return pkg, None
    except (KeyError, ValueError, TypeError):
        return None, "Invalid or missing parameters. Required: width, height, length, mass (numbers)."

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/classify', methods=['POST'])
def classify():
    try:
        pkg, err = parse_package_data(request.json)
        if err:
            return jsonify({"error": err}), 400
        return jsonify({"classification": pkg.classify()})
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)