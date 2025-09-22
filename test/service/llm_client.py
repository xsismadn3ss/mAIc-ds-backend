from g4f.client import ChatCompletionChunk, ChatCompletion, AsyncClient
from test.schema.llm import LLM_Message

class LLM_Client:
    def __init__(self, llm = AsyncClient()):
        self.llm = llm

    async def ask(self, message: LLM_Message):
        async for chunk  in self.llm.chat.completions.stream(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message.content}],
        ):
            if isinstance(chunk, ChatCompletionChunk):
                content = chunk.choices[0].delta.content
                if content is None:
                    yield ''
                else:
                    yield content
            elif isinstance(chunk, ChatCompletion):
                content = chunk.choices[0].message.content
                if content is None:
                    yield ''
                else:
                    yield content
            else:
                yield ''

def ai_dep():
    return LLM_Client()