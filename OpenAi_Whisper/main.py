import whisper

model = whisper.load_model("base")
result = model.transcribe("Transcribe Audio Files with OpenAI Whisper.mp3")

with open("transcription.txt","w") as f:
    f.write(result["text"])