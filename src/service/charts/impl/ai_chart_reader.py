from src.service.llm.impl.g4f_llm import G4f_LLM
from src.service.llm.abc_llm import ABC_LLM
from src.config.environment import AppEnv
from src.models.schema.llm_schema import LLM_Message
from src.models.schema.charts import Chart
from typing import List


class AI_ChartReader:
    def __init__(self, llm: ABC_LLM = G4f_LLM()) -> None:
        self.llm = llm
        super().__init__()

    async def read_charts(self, charts: List[Chart]) -> str:
        base_prompt: str = AppEnv().read_chart_prompt
        prompt: str = (
            f"{base_prompt}\nGráficas: {str([chart.model_dump() for chart in charts])}"
        )
        msg = LLM_Message(content=prompt)
        response = await self.llm.create(messages=[msg])
        return response


def ai_chart_reader_dep() -> AI_ChartReader:
    return AI_ChartReader()
