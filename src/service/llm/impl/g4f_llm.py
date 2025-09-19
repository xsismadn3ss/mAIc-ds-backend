from g4f.client import Client
from g4f import ChatCompletion
from src.models.schema.llm_schema import LLM_Message
from src.service.llm.abc_llm import ABC_LLM
from typing import List, override


class G4f_LLM(ABC_LLM):
    def __init__(self, client=Client()) -> None:
        self.client = client
        super().__init__()

    @override
    def create(self, messages: List[LLM_Message]) -> str:
        payload = []
        for m in messages:
            payload.append({"role": m.role, "content": m.content})

        response: ChatCompletion = self.client.chat.completions.create(
            model="gpt-4o-mini", messages=payload
        )

        choice: str = response.choices[0].message.content
        return choice


g4f_llm = lambda: G4f_LLM()
