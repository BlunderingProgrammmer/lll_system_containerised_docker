from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gtts import gTTS
from fastapi.staticfiles import StaticFiles
import os, json
from uuid import uuid4

app = FastAPI(title="Prompt-Voice-Memory")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}


os.makedirs("audio", exist_ok=True)
MEMORY_FILE = "memory_log.json"
if not os.path.exists(MEMORY_FILE):
    open(MEMORY_FILE, "w").close()


class ProcessRequest(BaseModel):
    session_id: str
    prompt: str
    response: str

class ProcessResponse(BaseModel):
    status: str
    audio_url: str

@app.post("/process", response_model=ProcessResponse)
async def process(req: ProcessRequest):
    fname = f"{uuid4()}.mp3"
    path = os.path.join("audio", fname)
    tts = gTTS(req.response)
    tts.save(path)

    
    entry = {"session_id": req.session_id, "prompt": req.prompt, "response": req.response}
    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return ProcessResponse(status="ok", audio_url=f"/audio/{fname}")


app.mount("/audio", StaticFiles(directory="audio"), name="audio")
