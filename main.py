from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from llama_cpp import Llama
import os

app = FastAPI(title="Llama Server")
templates = Jinja2Templates(directory="templates")
model = None  # Model instance placeholder


# Request model for /llama endpoint
class LlamaRequest(BaseModel):
    system_message: str
    user_message: str
    max_tokens: int


@app.get("/", response_class=HTMLResponse)
async def serve_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/llama")
async def generate_response(request: LlamaRequest):
    global model
    try:
        system_message = request.system_message
        user_message = request.user_message
        max_tokens = request.max_tokens

        prompt = f"""[INST] <<SYS>>
        {system_message}
        <</SYS>>
        {user_message} [/INST]"""

        if model is None:
            model_path = "./llama-2-7b-chat.Q2_K.gguf"
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found: {model_path}")
            model = Llama(model_path=model_path)

        output = model(prompt, max_tokens=max_tokens, echo=True)

        return {"response": output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
