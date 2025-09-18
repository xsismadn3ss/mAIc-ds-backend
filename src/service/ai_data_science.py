import json
from src.clients.ollama import ask
from src.config.environment import App_config
from src.models.schema.ollama import OllamaGenerateRequest


def analyze_df(columns, dtypes, describe):
    base_prompt = App_config.data_science_propmt

    # formater petición
    prompt = f"{base_prompt}\nColumnas: {str(columns)}\n\nTipos de datos: {str(dtypes)}\n\nResumen:{str(describe)}"
    payload = OllamaGenerateRequest(message=prompt)

    for chunk in ask(payload):
        r = chunk.get("response")
        if r:
            yield str(r)