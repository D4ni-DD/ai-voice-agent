from  dotenv import load_dotenv
import os
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()

# Initialize ElevenLabs client with API key from environment variable
elevenlabs=ElevenLabs(
    api_key=os.getenv("API_KEY_"),
)

# Generate speech from text using a specific voice and model
audio = elevenlabs.text_to_speech.convert(
    text="Olá, sou o ElevenLabs, um modelo de texto para fala.",
    ## voice_id="4CrZuIW9am7gYAxgo2Af", # English
    voice_id="UkO7OCLgMp3WYf4UPjE5",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

# Play the generated audio
play(audio)