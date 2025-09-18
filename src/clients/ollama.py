import json
import httpx
from src.config.environment import App_config
from src.models.schema.ollama import OllamaGenerateRequest

def ask(
    payload: OllamaGenerateRequest,
    pretty: bool = False,
):
    body = {
        "model": payload.model,
        "prompt": payload.message,
        "stream": True,
    }
    if payload.context:
        body["context"] = payload.context

    url = f"{App_config.ai_api_url.rstrip('/')}/generate"
    
    with httpx.stream("POST", url, json=body, timeout=None) as response:
        for line in response.iter_lines():
            if line:
                obj = json.loads(line)
                if pretty:
                    yield json.dumps(obj, ensure_ascii=False)
                else:
                    yield obj