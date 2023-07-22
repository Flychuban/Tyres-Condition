from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import glob
from model_setup import model_predict

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

    filename = f'png_{1}.png'
    saved_path = os.path.join(SAVED_DIR, filename)

    for file in files:
        filename = f'png_{1}.png'

        # Save the file to the "saved" directory
        file.save(saved_path)
        saved_files.append(saved_path)


    result = model_predict(saved_path)
    print(result)
    if result == "False":
        text = 'Гумата е в добро състояне'
    else:
        text = 'Гумата е в лошо състояне'
    

    return jsonify({'text': text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5677)  # Update the host and port as needed
