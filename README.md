# Jarvis - Voice Assistant using Python

Jarvis is a simple AI-powered voice assistant built with Python. It can recognize speech, respond using text-to-speech, open websites, tell the time, and interact with OpenAI's GPT model for intelligent responses.

## Features

- 🎤 Voice recognition using Google Speech Recognition
- 🗣️ Text-to-speech responses with Windows SAPI
- 🌐 Open popular websites or any site by name
- 🕒 Tell the current time
- 🤖 Chat mode using OpenAI GPT-3.5
- 📝 Save AI responses to files
- 🎵 Play local music files

## Installation

### Requirements

- Python 3.7+
- [OpenAI API Key](https://platform.openai.com/)
- Windows OS (due to `win32com.client` usage)

### Dependencies

Install the following Python libraries:

```bash
pip install SpeechRecognition pywin32 openai
```

## Setup

1. Clone the repository or copy the script.
2. Replace the OpenAI API key in the script:
   ```python
   openai.api_key = 'your-openai-api-key-here'
   ```
3. (Optional) Modify the music file path in the `open music` section to point to your own file.

## Usage

Run the script:

```bash
python jarvis.py
```

You will hear the voice assistant greet you and begin listening for commands.

### Example Commands

- "Open YouTube"
- "What is the time?"
- "Generate an article about AI"
- "Stop" – stops the assistant temporarily
- "Reset" – clears chat history
- "Quit" – exits the assistant

## Folder Structure

```
.
├── jarvis.py
├── openai/
│   └── prompt-<random_id>.txt
```

## Limitations

- Works only on Windows (due to SAPI usage).
- Requires an internet connection for speech recognition and OpenAI API calls.
- Basic error handling; may need enhancements for production use.

## Disclaimer

Make sure to keep your OpenAI API key secure and avoid hardcoding it in public repositories.

## License

This project is open-source and available under the MIT License.
