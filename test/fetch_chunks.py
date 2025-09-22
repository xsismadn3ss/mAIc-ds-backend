import time

import httpx
import asyncio

url = "http://localhost:8002/chat/completions"

payload = {
    "role": "user",
    "content": "Hola explicarme que es una red p2p"
}

# respuesta asíncrona
async def fetch_chunks():
    # evitar maximo tiempo de espera
    async with httpx.AsyncClient(timeout=300) as client:
        async with client.stream("POST", url, json=payload) as response:
            async for chunk in response.aiter_text():
                print(chunk, end="")


if __name__ == '__main__':
    asyncio.run(fetch_chunks())