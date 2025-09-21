"""Esquemas de datos para el mensaje"""
from pydantic import BaseModel, Field

class Message(BaseModel):
    message: str = Field(default="", description="Content of the message")