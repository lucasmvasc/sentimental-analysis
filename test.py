import requests

API_URL = "https://8d29-187-18-138-207.ngrok-free.app/analyze"  
API_KEY = "123456"

audio_file = "audio/agendamento_de_reuniao.mp3"
files = {"audio": open(audio_file, "rb")}

response = requests.post(
    API_URL,
    headers={"Api-Key": API_KEY},
    files=files
)

print(response.text)