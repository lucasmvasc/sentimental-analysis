import os
import json
from flask import Flask, request, jsonify
from models.transcription import get_text_from
from models.sentiment_analysis import get_sentiments_from

with open('secrets.json', 'r') as file:
    secrets = json.load(file)
API_KEY = secrets.get('API_KEY', None)

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():

    # API Key verification
    key = request.headers.get('Api-Key')
    if key != API_KEY:
        return jsonify({"error": "Invalid api key"}), 401
    else:
        print("Chave API Válida")

    # Audio transcription
    audio = request.files['audio']
    content = get_text_from(audio)

    # Audio segments treatment
    msg_segments = [segment['text'] for segment in content['segments']]

    # Sentimental Analysis
    result = get_sentiments_from(msg_segments)

    return result

if __name__ == "__main__":
   app.run()