"""Esquemas de datos para el LLM"""

from pydantic import BaseModel, Field


class LLM_Message(BaseModel):
    role: str = Field(description="rol del usuario en la petición", default="user")
    content: str = Field(description="contenido del mensaje")


class LLM_Response(BaseModel):
    role: str = Field(description="rol de la respuesta", default="assistant")
    content: str = Field(description="contenido de la respuesta")
