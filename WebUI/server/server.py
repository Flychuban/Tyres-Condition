from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import glob

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

text = ''

SAVED_DIR = 'saved'  # Update the SAVED_DIR to 'saved'

def check_newest_file():
    files = sorted(os.listdir(SAVED_DIR))
    newest_file = files[-1] if files else None

    return newest_file or 'No files found'

@app.route('/submit', methods=['POST'])
def submit_form():
    files = request.files.getlist('file')

    # Create the "saved" directory if it doesn't exist
    if not os.path.exists(SAVED_DIR):
        os.makedirs(SAVED_DIR)

    saved_files = []

    # Get the count of existing files in the "saved" directory
    existing_files = glob.glob(os.path.join(SAVED_DIR, '*.png'))
    file_count = len(existing_files)

    for file in files:
        file_count += 1
        filename = f'png_{file_count}.png'
        saved_path = os.path.join(SAVED_DIR, filename)

        # Save the file to the "saved" directory
        file.save(saved_path)
        saved_files.append(saved_path)

    return jsonify({'message': 'Files saved successfully.', 'saved_files': saved_files})

@app.route('/get', methods=['GET'])
def get():
    newest_file = check_newest_file()
    if newest_file:
        file_path = os.path.join(SAVED_DIR, newest_file)
        return send_file(file_path, as_attachment=True)
    else:
        return 'No files found'
    
@app.route('/send_prediction', methods=['POST'])
def send_string():
    text = request.json.get('text')  # Get the string value from the request JSON data
    return jsonify({'message': 'String received successfully.', 'text': text})

@app.route('/check_text', methods=['GET'])
def set_pending():
    if text != '':
        return jsonify({'text': text})    
    return jsonify({'status': "False"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5677)  # Update the host and port as needed
