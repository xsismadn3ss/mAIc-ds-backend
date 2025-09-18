from typing import List
from pydantic import BaseModel, Field
from src.config.environment import App_config

class OllamaGenerateRequest(BaseModel):
    model: str = Field(default=App_config.ai_model)
    message: str = Field()
    context: List[int] = Field(default=None)
    stream: bool = Field(default=True)