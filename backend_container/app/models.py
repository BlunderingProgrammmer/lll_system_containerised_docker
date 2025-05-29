from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_response(prompt: str, max_length: int = 50) -> dict:
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids,
            max_length=max_length,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {
        "response": response[len(prompt):],  
        "tokens_used": len(outputs[0])
    }