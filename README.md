# Voice-Activated Personal Assistant

## Overview
The **Voice-Activated Personal Assistant** is a Python-based virtual assistant that can perform various tasks based on voice commands. It uses speech recognition to process user input and responds with appropriate actions such as web searches, opening applications, fetching weather updates, and more.

## Features
- Speech recognition and text-to-speech functionality
- Open websites and applications
- Fetch weather updates
- Perform Google searches
- Send emails (configurable)
- Set reminders and alarms
- Play music

## Technologies Used
- Python
- SpeechRecognition (for voice input)
- pyttsx3 (for text-to-speech conversion)
- Wikipedia API (for fetching information)
- OpenWeatherMap API (for weather updates)
- smtplib (for sending emails)
- os, subprocess (for opening applications)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure API keys (if required) in `config.py`.
4. Run the assistant:
   ```sh
   python assistant.py
   ```

## Usage
1. Run the script and speak into the microphone.
2. Use commands like:
   - "Open Google"
   - "What's the weather like?"
   - "Search Wikipedia for Python programming"
   - "Send an email"
   - "Play music"
3. The assistant will process the command and respond accordingly.

## Configuration
- **Email settings**: Modify the `send_email()` function in `assistant.py` to configure email credentials.
- **API Keys**: Set your OpenWeatherMap API key in `config.py` for weather-related queries.

## Contributing
If you'd like to contribute, please fork the repository and submit a pull request.





