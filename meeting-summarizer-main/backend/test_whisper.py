from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe("harvard.wav")

print(f"Detected language: {info.language}")
print(f"Language probability: {info.language_probability:.2f}")
print("\nTranscript:\n")

for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")