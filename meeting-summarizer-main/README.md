# Meeting Summarizer

An AI-powered meeting summarization application that transcribes meeting audio and generates an action-oriented summary, including key decisions and action items.

## Features

- Upload a meeting audio file
- Transcribe meeting audio using faster-whisper
- Generate an AI-powered meeting summary
- Identify key decisions
- Identify action items
- Simple web interface for uploading audio and viewing results
- Local AI processing without paid external AI APIs

## Technologies Used

- Python
- FastAPI
- faster-whisper
- Ollama
- Gemma 3 4B
- HTML
- CSS
- JavaScript

## Project Structure

```text
meeting-summarizer/
│
├── backend/
│   ├── main.py
│   ├── transcription.py
│   ├── summarization.py
│   ├── test_whisper.py
│   └── test_summarization.py
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md
```

## How It Works

The application processes a meeting recording through the following pipeline:

```text
Meeting Audio
      ↓
    FastAPI
      ↓
faster-whisper
      ↓
   Transcript
      ↓
   Gemma 3 4B
      ↓
Summary + Key Decisions + Action Items
```

### 1. Audio Upload

The user selects a meeting audio file through the web interface.

### 2. Speech-to-Text

FastAPI receives the audio file and passes it to faster-whisper.

faster-whisper converts the meeting audio into a text transcript.

### 3. Meeting Summarization

The transcript is sent to a locally running Gemma 3 4B model through Ollama.

The model generates:

- Summary
- Key Decisions
- Action Items

### 4. Results

The transcript and generated summary are displayed on the web interface.

## Requirements

The following software is required:

- Python 3.13
- Ollama
- Gemma 3 4B model

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Anurag-Kakoty/meeting-summarizer.git
cd meeting-summarizer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

After activation, the terminal should show:

```text
(venv)
```

### 4. Install Python Dependencies

Install the required packages:

```bash
pip install fastapi uvicorn python-multipart faster-whisper requests
```

### 5. Install Ollama and the Gemma Model

Install Ollama and download the Gemma 3 4B model:

```bash
ollama pull gemma3:4b
```

Verify that the model is installed:

```bash
ollama list
```

The output should include:

```text
gemma3:4b
```

## Running the Application

### 1. Start the Backend

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Navigate to the backend directory:

```bash
cd backend
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

The FastAPI documentation can also be accessed at:

```text
http://127.0.0.1:8000/docs
```

### 2. Open the Frontend

Open the following file in a web browser:

```text
frontend/index.html
```

Select a meeting audio file and click:

**Summarize Meeting**

The application will process the recording and display the transcript and AI-generated summary.

## AI Processing

### Speech Recognition

The application uses faster-whisper for automatic speech recognition.

The model runs locally and converts the uploaded meeting recording into a text transcript.

### Large Language Model

The application uses Gemma 3 4B through Ollama for meeting summarization.

The model is prompted to generate:

1. A concise summary
2. Key decisions
3. Action items

The prompt instructs the model not to invent information that is not present in the transcript.

## Testing

The application was tested to verify:

- Meeting audio transcription
- Language detection
- Transcript generation
- AI summary generation
- Key decision identification
- Action item identification
- Frontend-to-backend communication

Both the transcription and summarization components also include separate test scripts.

## Local Processing

The application uses locally running AI models for both transcription and summarization.

No paid external AI API is required.

Meeting audio is temporarily stored during processing and removed after the request is completed.

## Limitations

- Processing time depends on the length of the meeting recording and the computer hardware.
- Summary quality depends on the quality and accuracy of the generated transcript.
- The application is intended as a simple assignment implementation rather than a production meeting management system.
