import asyncio
import websockets
import json
import os
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

async def test():
    uri = "wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id=scribe_v2_realtime&audio_format=ulaw_8000&language_code=en"
    try:
        async with websockets.connect(uri, additional_headers={"xi-api-key": ELEVENLABS_API_KEY}) as ws:
            await ws.send(json.dumps({"message_type": "input_audio_chunk", "audio_base_64": "A" * 100}))
            while True:
                response = await ws.recv()
                print("STT Response:", response)
                break
    except Exception as e:
        print("Error:", e)

asyncio.run(test())
