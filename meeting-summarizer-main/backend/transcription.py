from faster_whisper import WhisperModel


model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path: str) -> dict:
    segments, info = model.transcribe(audio_path)

    transcript = " ".join(segment.text.strip() for segment in segments)

    return {
        "language": info.language,
        "language_probability": info.language_probability,
        "transcript": transcript
    }