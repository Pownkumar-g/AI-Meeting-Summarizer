import os

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from transcription import transcribe_audio
from summarization import summarize_transcript


app = FastAPI(title="Meeting Summarizer")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Meeting Summarizer API is running"}


@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    audio_path = f"temp_{file.filename}"

    try:
        with open(audio_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        transcription_result = transcribe_audio(audio_path)

        summary = summarize_transcript(
            transcription_result["transcript"]
        )

        return {
            "filename": file.filename,
            "language": transcription_result["language"],
            "language_probability": transcription_result["language_probability"],
            "transcript": transcription_result["transcript"],
            "summary": summary
        }

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)