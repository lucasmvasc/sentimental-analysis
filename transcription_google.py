import os
from flask import Flask, request, jsonify
import pydub
import speech_recognition as sr

API_KEY = "123"
app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    key = request.headers.get('Api-Key')
    if key != API_KEY:
        return jsonify({"error": "Invalid api key"}), 401
    print("Chave API Válida")
    audio = request.files['audio']
    

    # 2. Ler o arquivo MP3 enviado na requisição:

    with open('audio.wav', 'wb') as f:
        f.write(audio.stream.read())

    # 3. Extrair o texto do áudio MP3 usando Speech Recognition

    recognize = sr.Recognizer()
    with sr.AudioFile('audio.wav') as source:
        print("Start talking: ")
        audio = recognize.record(source)
        print("Stop talking.")

        try:
            text = recognize.recognize_google(audio, language='pt-BR', show_all=True)
            print(text)
        except Exception as e:
            print (e)

    os.remove("audio.wav")

    return text

# 4. Com o texto extraído, podemos seguir com a análise de sentimentos como antes

# 5. O cliente pode enviar o MP3 assim:

if __name__ == "__main__":
   app.run()