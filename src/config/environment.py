"""
Variables de entorno del proyecto cargadas en memoria
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class AppEnv:
    simple_chart_prompt: str = os.environ["SIMPLE_CHART_PROMPT"]
    read_chart_prompt: str = os.environ["READ_CHART_PROMPT"]
