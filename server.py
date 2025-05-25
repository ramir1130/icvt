import os
import hashlib
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import imagehash

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DB_FOLDER = 'db'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DB_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    if 'image' not in request.files:
        return jsonify({'error': 'Нет файла'})

    file = request.files['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Хешим картинку
    uploaded_hash = imagehash.average_hash(Image.open(filepath))

    for db_filename in os.listdir(DB_FOLDER):
        db_path = os.path.join(DB_FOLDER, db_filename)
        db_hash = imagehash.average_hash(Image.open(db_path))

        # Чем меньше расстояние — тем ближе
        if uploaded_hash - db_hash < 5:
            return jsonify({'found': True, 'filename': db_filename})

    return jsonify({'found': False})

if __name__ == '__main__':
    app.run(debug=True)
