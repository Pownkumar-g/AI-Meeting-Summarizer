# AI Meeting Summarizer

An AI-powered web application that converts meeting audio into text and generates a structured, easy-to-understand summary. The system also extracts important decisions and action items from the meeting, helping users quickly understand the key outcomes without listening to the entire recording.

The application performs all major AI processing locally, avoiding the need for paid third-party AI APIs.

## Features

* Upload meeting audio files through a web interface
* Convert meeting audio into text automatically
* Generate an AI-based summary of the discussion
* Extract important decisions made during the meeting
* Identify tasks and action items
* Display both the complete transcript and summarized results
* Simple and user-friendly web interface
* Local AI-based processing
* No paid external AI API required

## Technologies Used

* **Python** – Backend development and AI integration
* **FastAPI** – Backend API framework
* **faster-whisper** – Speech-to-text transcription
* **Ollama** – Local LLM execution
* **Gemma 3 4B** – AI model used for summarization
* **HTML** – Frontend structure
* **CSS** – User interface styling
* **JavaScript** – Frontend functionality and API communication

## Project Structure

```text
AI-Meeting-Summarizer/
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

## How the Application Works

The application follows a simple AI processing pipeline:

```text
Meeting Audio
      ↓
Upload through Web Interface
      ↓
FastAPI Backend
      ↓
faster-whisper
      ↓
Text Transcript
      ↓
Ollama + Gemma 3 4B
      ↓
Meeting Summary
      ↓
Key Decisions + Action Items
```

## Working Process

### 1. Upload Meeting Audio

The user uploads a recorded meeting audio file using the web interface.

The frontend sends the selected audio file to the FastAPI backend for processing.

### 2. Audio Transcription

After receiving the audio file, the backend passes it to the **faster-whisper** model.

The speech recognition model processes the audio and converts the spoken conversation into a text transcript.

### 3. AI-Based Summarization

The generated transcript is sent to the **Gemma 3 4B** language model running locally through **Ollama**.

The AI model analyzes the meeting discussion and generates structured output containing:

* Meeting Summary
* Key Decisions
* Action Items

The AI is instructed to generate information based only on the provided transcript.

### 4. Displaying the Results

Once processing is completed, the application returns the results to the frontend.

The user can view:

* Full Meeting Transcript
* AI-Generated Summary
* Important Decisions
* Action Items

## Requirements

Before running the project, make sure the following software is installed on your system:

* Python 3.13
* Ollama
* Gemma 3 4B model
* Required Python libraries

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
cd AI-Meeting-Summarizer
```

### Step 2: Create a Virtual Environment

Create a Python virtual environment using:

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

After activation, the terminal should display something similar to:

```text
(venv)
```

### Step 4: Install Required Dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn python-multipart faster-whisper requests
```

## Installing the AI Model

### Step 5: Install Ollama

Install Ollama on your system and make sure it is running.

### Step 6: Download the Gemma Model

Run the following command:

```bash
ollama pull gemma3:4b
```

To verify that the model has been downloaded successfully, run:

```bash
ollama list
```

The installed models should include:

```text
gemma3:4b
```

## Running the Application

### Step 1: Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### Step 2: Navigate to the Backend Folder

```bash
cd backend
```

### Step 3: Start the FastAPI Server

Run:

```bash
uvicorn main:app --reload
```

The backend server will start locally.

The application backend can be accessed at:

```text
http://127.0.0.1:8000
```

FastAPI interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### Step 4: Open the Frontend

Open the following file in a web browser:

```text
frontend/index.html
```

Select a meeting audio file and click the **Summarize Meeting** button.

The system will process the audio and display the transcript along with the AI-generated meeting analysis.

## AI Processing

### Speech-to-Text Model

The project uses **faster-whisper** for automatic speech recognition.

It processes the uploaded meeting audio locally and converts spoken content into a text transcript.

### Large Language Model

The application uses **Gemma 3 4B** through **Ollama** for natural language processing and summarization.

The model is responsible for generating:

1. A concise summary of the meeting
2. Important decisions discussed during the meeting
3. Action items and assigned tasks

The summarization prompt is designed to reduce the generation of information that is not present in the original meeting transcript.

## Testing

The project was tested for the following functionalities:

* Audio file upload
* Backend API processing
* Speech-to-text transcription
* Language detection
* Transcript generation
* AI-generated meeting summaries
* Key decision extraction
* Action item identification
* Communication between frontend and backend

Separate test files are also included to verify the transcription and summarization modules individually.

## Local AI Processing

This project is designed to run AI models locally.

Both the speech recognition and language model processing are performed on the user's system.

This provides several benefits:

* No paid AI API subscription is required
* Meeting data does not need to be sent to an external AI service
* Users have more control over their data
* The project can be used for learning and experimentation with local AI models

Uploaded audio files are used temporarily during processing and can be removed after the request is completed.

## Limitations

* Processing speed depends on the computer's hardware specifications.
* Longer meeting recordings require more processing time.
* Transcription accuracy depends on audio quality, background noise, accents, and clarity of speech.
* The quality of the generated summary depends on the accuracy of the transcript.
* The Gemma 3 4B model may require sufficient system memory and computing resources.
* This project is intended as a learning and academic implementation and does not currently include advanced enterprise features such as user authentication, cloud storage, speaker identification, or real-time meeting transcription.

## Future Improvements

Possible future enhancements include:

* Real-time meeting transcription
* Speaker identification
* Support for multiple audio and video formats
* Download summaries as PDF or DOCX files
* User authentication and account management
* Meeting history storage
* Cloud deployment
* Multi-language support
* Emailing meeting summaries automatically
* Calendar and video meeting platform integration
* Improved action item tracking

## Conclusion

**AI Meeting Summarizer** demonstrates how Speech Recognition and Large Language Models can be combined to solve a practical real-world problem.

The application converts meeting recordings into text using **faster-whisper** and uses **Gemma 3 4B through Ollama** to generate meaningful summaries, identify important decisions, and extract actionable tasks.

By running the AI models locally, the project provides a simple and cost-effective approach to intelligent meeting analysis without depending on paid external AI APIs.
