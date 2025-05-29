from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import generate_response
from app.schemas import PromptRequest, LLMResponse

app = FastAPI(title="LLM Backend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"msg": "pong"}

@app.post("/generate", response_model=LLMResponse)
async def generate(prompt_data: PromptRequest):
    result = generate_response(
        prompt=prompt_data.prompt,
        max_length=prompt_data.max_length
    )
    return result
