import requests

API_URL = "https://8654-187-18-138-207.ngrok-free.app/analyze"  
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