import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class AppEnv:
    ai_model: str = os.environ["AI_MODEL"]
    ai_api_url: str = os.environ["AI_API_URL"]
    simple_chart_prompt: str = os.environ["SIMPLE_CHART_PROMPT"]
