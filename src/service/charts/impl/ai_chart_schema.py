from src.service.charts.abc_chart_schema import ABC_Chart_Schema
from src.service.llm.impl.g4f_llm import G4f_LLM
from src.service.llm.abc_llm import ABC_LLM
from src.config.environment import App_config
from src.models.schema.llm_schema import LLM_Message
from typing import override
import json
from fastapi import HTTPException


class AI_Chart_Schema(ABC_Chart_Schema):
    def __init__(self, llm:ABC_LLM = G4f_LLM()) -> None:
        self.llm = llm
        super().__init__()

    @override
    def build_schemas(self, columns, dtypes, describe):
        base_propmt: str = App_config.data_science_propmt

        prompt: str = (
            f"{base_propmt}\nColumnas: {str(columns)}\n\nTipos de datos: {str(dtypes)}\n\nResumen: {str(describe)}"
        )

        msg = LLM_Message(content=prompt)
        response = self.llm.create(messages=[msg])
        print(response)

        try:
            return json.loads(response)
        except Exception as e:
            print(type(e))
            raise HTTPException(500, e)
