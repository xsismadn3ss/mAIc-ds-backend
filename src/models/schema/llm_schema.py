from pydantic import BaseModel, Field

class LLM_Message(BaseModel):
    role: str = Field(description="rol del usuario en la petición", default="user")
    content: str = Field(description="contenido del mensaje")