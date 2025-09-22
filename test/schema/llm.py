from pydantic import BaseModel, Field

class LLM_Message(BaseModel):
    role: str = Field(description="Role of the message", default="user")
    content: str = Field(description="Content of the message", default="Hello world")

class Message(BaseModel):
    propmt: str = Field(description="Prompt of the message", default="Smile Face")