import asyncio
import websockets
import os
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

async def test():
    uri = "wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id=scribe_v2_realtime&audio_format=ulaw_8000&language_code=en"
    try:
        async with websockets.connect(uri, additional_headers={"xi-api-key": ELEVENLABS_API_KEY}) as ws:
            print("Connected!")
            await ws.close()
    except Exception as e:
        print("Error:", e)

asyncio.run(test())
