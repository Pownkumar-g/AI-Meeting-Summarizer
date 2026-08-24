import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"


def summarize_transcript(transcript: str) -> str:
    prompt = f"""
You are a meeting summarization system.

Analyze the meeting transcript below.

Return ONLY the following three sections, in exactly this order:

1. Summary
Write a concise summary of the main topics discussed.

2. Key Decisions
List decisions explicitly made during the meeting.
If no decisions were made or identified, write:
None identified.

3. Action Items
List tasks that were assigned or agreed upon.
For each task, include the responsible person and deadline when explicitly stated.
Do not invent a person or deadline.
If no action items were identified, write:
None identified.

IMPORTANT:
- Do not add an introduction or conclusion.
- Do not add any sections other than the three requested sections.
- Do not invent information.
- Only use information contained in the transcript.

Meeting transcript:
{transcript}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()

    return response.json()["response"]