import modal
from fastapi import Request, Response

app = modal.App("qwen-tts-server")

image = modal.Image.debian_slim().pip_install("edge-tts", "fastapi")

@app.function(image=image)
@modal.fastapi_endpoint(method="POST")
async def synthesize(request: Request):
    data = await request.json()
    text = data.get("text", "Hello from Modal TTS")
    voice_id = data.get("voice_id", "en-US-AriaNeural")
    
    import edge_tts
    import tempfile
    
    communicate = edge_tts.Communicate(text, voice_id)
    
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        temp_path = f.name
        
    await communicate.save(temp_path)
    
    with open(temp_path, "rb") as f:
        audio_bytes = f.read()
        
    return Response(content=audio_bytes, media_type="audio/wav")
