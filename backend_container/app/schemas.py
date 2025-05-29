from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 50  

class LLMResponse(BaseModel):
    response: str
    tokens_used: int