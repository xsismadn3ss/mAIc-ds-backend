from abc import ABC, abstractmethod
from typing import Any

from fastapi import UploadFile
from src.models.schema.charts import Chart


class ABC_ChartBuilder(ABC):
    @abstractmethod
    async def build_chart(
        self, file: UploadFile, title:str, chart_type:str, parameter: str
    ) -> Chart:
        raise NotImplementedError()
