import re
from pandas import DataFrame
from src.models.schema.charts import (
    Chart,
    ChartParameter,
)
from ..abc_chart_builder import ABC_ChartBuilder
from .chart_data_processor import ChartDataProcessor
from src.service.pipe.impl.pandas_pipe import PandasPipe
from ...statistics.impl.statistics import Statistics
from typing import override, List


def clean(value: str):
    return re.sub(r'\s*\(.*?\)', '', value).strip()

class ChartBuilder(ABC_ChartBuilder):
    def __init__(self, pipe: PandasPipe, chart_data_processor: ChartDataProcessor):
        self.pipe = pipe
        self.chart_data_processor = chart_data_processor

    @override
    def build_chart(
        self, df: DataFrame, title: str, chart_type: str, parameter: List[ChartParameter], mesure:str
    ) -> Chart:
        data_processed = self.chart_data_processor.process_parameters(df, parameter, mesure)

        return Chart(title=title, chart_type=chart_type, data=data_processed)


def chart_builder_dep():
    statistics_instance = Statistics()
    chart_data_processor_instance = ChartDataProcessor(statistics_instance)
    return ChartBuilder(PandasPipe(), chart_data_processor_instance)
