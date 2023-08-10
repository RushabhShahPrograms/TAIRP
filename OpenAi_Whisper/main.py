<<<<<<< HEAD
import whisper

model = whisper.load_model("base")
result = model.transcribe("Transcribe Audio Files with OpenAI Whisper.mp3")

with open("transcription.txt","w") as f:
=======
import whisper

model = whisper.load_model("base")
result = model.transcribe("Transcribe Audio Files with OpenAI Whisper.mp3")

with open("transcription.txt","w") as f:
>>>>>>> 0fb0c66000e07c1d11087329b62690269a8180e7
    f.write(result["text"])