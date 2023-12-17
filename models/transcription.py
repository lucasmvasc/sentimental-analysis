import os
import whisper

model = whisper.load_model("small")

def get_text_from(audio):
    # Create uploads folder if not exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    # Save the file to uploads folder
    audio_path = os.path.join('uploads', audio.filename) 
    audio.save(audio_path)

    # Execute model on MP3 File - get audio transcript
    result = model.transcribe(f"uploads/{audio.filename}", language="pt", fp16=False, verbose=True)
    full_message_ctn = result["text"]

    os.remove(f"uploads/{audio.filename}")

    return result