import time
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
import os
import threading
from dotenv import load_dotenv

load_dotenv()

# Initialize ElevenLabs client with API key from environment variable
client = ElevenLabs(api_key=os.getenv("API_KEY_"))

audio_interface = DefaultAudioInterface()

# Ensure the audio_interface has the necessary attributes for safe stopping
if not hasattr(audio_interface, 'should_stop'):
    audio_interface.should_stop = threading.Event()
if not hasattr(audio_interface, '_output_thread'):
    audio_interface._output_thread = None
if not hasattr(audio_interface, 'output_thread'):
    audio_interface.output_thread = None

# Define a safe stop method to ensure threads are properly joined
def safe_stop(self):
    if hasattr(self, 'should_stop'):
        self.should_stop.set()
    if hasattr(self, 'output_thread') and self.output_thread is not None:
        self.output_thread.join()

# Bind the safe_stop method to the audio_interface instance
audio_interface.stop = safe_stop.__get__(audio_interface)

# Create a conversation instance with the client, agent ID, and audio interface
conversation = Conversation(
    client=client,
    agent_id="agent_2101k5c417rteqprp66xmnhzx5rn",
    requires_auth=True,
    audio_interface=audio_interface,
)

# Start the conversation session
conversation.start_session()

# conversation between user and AI
try:
    print("Active conversation. Type your messages below (Ctrl+C to exit):")
    while True:
        user_input = input("You: ")
        response = conversation.send_user_message(user_input)
except KeyboardInterrupt:
    print("Ending conversation...")
finally:
    # Ensure the session is properly ended
    conversation.end_session()

