import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class App_config:
    ai_model: str = os.environ["AI_MODEL"]
    ai_api_url: str = os.environ["AI_API_URL"]
    data_science_propmt: str = os.environ["DATA_SCIENCE_PROPMT"]