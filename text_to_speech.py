from  dotenv import load_dotenv
import os
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()

elevenlabs=ElevenLabs(
    api_key=os.getenv("API_KEY_"),
)


audio = elevenlabs.text_to_speech.convert(
    text="Olá, sou o ElevenLabs, um modelo de texto para fala.",
    ## voice_id="4CrZuIW9am7gYAxgo2Af", # English
    voice_id="UkO7OCLgMp3WYf4UPjE5",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)