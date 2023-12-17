import requests

API_URL = "http://localhost:5000/analyze"  
API_KEY = "123456"

audio_file = "audio/agendamento_de_reuniao.mp3"

data = {"conversation_id": "123"}
files = {"audio": open(audio_file, "rb")}

response = requests.post(
    API_URL,
    headers={"Api-Key": API_KEY},
    data=data,
    files=files
)

print(response.text)