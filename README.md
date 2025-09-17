# Conversational AI Voice Assistant with ElevenLabs - Python
This project demonstrates how to create a basic conversational AI voice assistant using the ElevenLabs API and Python.

## Features
- Connects to ElevenLabs Conversational AI platform with API authentication
- Supports real-time audio input/output through a default audio interface
- Implements a conversation session with an agent using an agent ID
- Includes a patched audio interface stop method to avoid threading errors
- Provides an interactive text input loop for sending messages and receiving responses
- Gracefully handles session start and end with user interruption (Ctrl+C)

## Requirements
- Python 3.8 or later
- ElevenLabs Python SDK
- python-dotenv for environment variable loading
- threading (standard Python library)
- Valid ElevenLabs API key stored in .env as API_KEY_

## Usage
1. Install dependencies:
pip install elevenlabs python-dotenv

2. Create a .env file in the project root containing your API key:
API_KEY_=your_elevenlabs_api_key_here

3. Run the script:
python conversation.py

4. Type your messages interactively or talk; the assistant will respond through the conversational AI agent.

5. Press Ctrl+C to end the conversation session gracefully.

## Code Highlights
- Initializes the ElevenLabs client with API key management
- Sets up an audio interface to handle voice input/output and patches methods to avoid runtime errors
- Creates a Conversation instance with authentication and audio interface
- Starts the session and enters an interactive loop to send user messages and receive responses
- Properly stops the session on user interruption

## Notes
Ensure your ElevenLabs agent ID is valid and configured correctly
This example uses text input; audio input/output requires additional setup and dependencies
Consult ElevenLabs documentation for advanced usage, events, and streaming conversation
