import asyncio
import websockets
import json
import os
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "pNInz6obpgDQGcFmaJgB"

async def test():
    uri = f"wss://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream-input?model_id=eleven_turbo_v2&output_format=ulaw_8000"
    try:
        async with websockets.connect(uri, additional_headers={"xi-api-key": ELEVENLABS_API_KEY}) as ws:
            await ws.send(json.dumps({"text": "Hello ", "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}}))
            await ws.send(json.dumps({"text": ""}))
            while True:
                response = await ws.recv()
                data = json.loads(response)
                print("Response data:", data)
                if data.get("isFinal") or data.get("error"):
                    break
    except Exception as e:
        print("Exception:", e)

asyncio.run(test())
