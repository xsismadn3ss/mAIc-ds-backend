from g4f.client import Client
from g4f import ChatCompletion
from src.models.schema.llm_schema import LLM_Message
from src.service.llm.abc_llm import ABC_LLM
from typing import List, override
import asyncio
import concurrent.futures


class G4f_LLM(ABC_LLM):
    def __init__(self, client=Client()) -> None:
        self.client = client
        super().__init__()

    def _sync_create(self, messages: List[LLM_Message]) -> str:
        """Método síncrono para llamar a g4f"""
        payload = []
        for m in messages:
            payload.append({"role": m.role, "content": m.content})

        response: ChatCompletion = self.client.chat.completions.create(
            model="gpt-4o-mini", messages=payload
        )

        choice: str = response.choices[0].message.content
        return choice

    @override
    async def create(self, messages: List[LLM_Message]) -> str:
        """Método asíncrono que ejecuta la llamada síncrona en un hilo separado"""
        loop = asyncio.get_event_loop()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result = await loop.run_in_executor(executor, self._sync_create, messages)
        return result


g4f_llm = lambda: G4f_LLM()
