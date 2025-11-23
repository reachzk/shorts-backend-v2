from fastapi import FastAPI, File, UploadFile
from moviepy.editor import VideoFileClip
import uuid
import os

app = FastAPI()

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}.mp4"
    with open(filename, "wb") as f:
        f.write(await file.read())

    # cortar o vídeo
    clip = VideoFileClip(filename)
    subclip = clip.subclip(0, min(clip.duration, 30))
    output = f"output_{filename}"
    subclip.write_videofile(output)

    return {"message": "OK", "file": output}
