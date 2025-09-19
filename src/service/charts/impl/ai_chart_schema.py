from src.service.charts.abc_chart_schema import ABC_ChartSchema
from src.service.llm.impl.g4f_llm import G4f_LLM
from src.service.llm.abc_llm import ABC_LLM
from src.config.environment import AppEnv
from src.models.schema.llm_schema import LLM_Message
from src.models.schema.charts import ChartSchema
from typing import override, List
import json
from fastapi import HTTPException


class AI_ChartSchema(ABC_ChartSchema):
    def __init__(self, llm: ABC_LLM = G4f_LLM()) -> None:
        self.llm = llm
        super().__init__()

    @override
    def build_schema(self, columns, dtypes, describe) -> List[ChartSchema]:
        base_prompt: str = AppEnv.simple_chart_prompt
        prompt: str = (
            f"{base_prompt}\nColumnas: {str(columns)}\n\nTipos de datos: {str(dtypes)}\n\nResumen: {str(describe)}"
        )
        msg = LLM_Message(content=prompt)
        response = self.llm.create(messages=[msg])

        try:
            data: dict = json.loads(response)
            return [ChartSchema(**d) for d in data.get("charts")]
        except Exception as e:
            print(type(e))
            raise HTTPException(500, e)


ai_chart_schema = lambda: AI_ChartSchema()
