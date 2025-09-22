from fastapi.params import Depends
from fastapi import FastAPI
from test.service.llm_client import LLM_Client, ai_dep
from test.schema.llm import LLM_Message
from starlette.responses import StreamingResponse

app = FastAPI(
    title="AI Stream API",
    description="API para realizar peticiones asíncronas a un modelo de AI.",
)

@app.post(
    path="/chat/completions",
    description="Preguntar a un modelo",
    response_description="En stream de texto plano"
)
async def ask_model(message: LLM_Message, ai:LLM_Client = Depends(ai_dep)) -> StreamingResponse:
    return StreamingResponse(ai.ask(message), media_type="text/event-stream")