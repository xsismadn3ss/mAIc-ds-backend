from abc import ABC, abstractmethod
from pandas import DataFrame
from src.models.schema.charts import Chart


class ABC_ChartBuilder(ABC):
    @abstractmethod
    def build_chart(
        self, df: DataFrame, title:str, chart_type:str, parameter: str
    ) -> Chart:
        raise NotImplementedError()
