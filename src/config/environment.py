import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class AppEnv:
    simple_chart_prompt: str = os.environ["SIMPLE_CHART_PROMPT"]
    allowed_origins: str = os.environ["ALLOWED_ORIGINS"]
