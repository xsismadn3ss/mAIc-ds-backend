import re

from fastapi import UploadFile
from src.models.schema.charts import Chart, ChartParameter, ParameterProccesed, DataValue
from ..abc_chart_builder import ABC_ChartBuilder
from src.service.pipe.impl.pandas_pipe import PandasPipe
from typing import override, List
import pandas as pd
import json

from ...statistics.impl.statistics import statistics_dep, Statistics


def _check_columns(params: List[ChartParameter], df: pd.DataFrame):
    for param in params:
        x = re.sub(r"\s*\(.*?\)", "", param.x_axis)
        if x not in df.columns:
            raise ValueError(f"Columna {x} no existe")
        y = re.sub(r"\s*\(.*?\)", "", param.y_axis)
        if y not in df.columns:
            raise ValueError(f"Columna {y} no existe")


def _convert_params(params: str):
    data = json.loads(params)
    return [ChartParameter(**d) for d in data]


class ChartBuilder(ABC_ChartBuilder):
    def __init__(self,
                 pipe: PandasPipe = PandasPipe(),
                 statistics: Statistics = Statistics()) -> None:
        self.pipe = pipe
        self.statistics = statistics
        super().__init__()

    @override
    async def build_chart(
            self, file: UploadFile, title: str, chart_type: str, parameter: str
    ) -> Chart:
        """
        Construir gráfica con los datos de un archivo
        :param file: archivo a analizar
        :param title: título de la gráfica
        :param chart_type: tipo de gráfica
        :param parameter: parámetros de la gráfica
        :return:
        """
        # convertir parametro
        chart_params = _convert_params(parameter)
        df: pd.DataFrame = await self.pipe.generate_df(file)
        _check_columns(chart_params, df)

        data: List[ParameterProccesed] = []
        for param in chart_params:
            param_data = []
            for _, row in df.iterrows():
                param_data.append(DataValue(
                    x=row[param.x_axis],
                    y=row[param.y_axis]
                ))
            processed_param = ParameterProccesed(
                x_axis=param.x_axis,
                y_axis=param.y_axis,
                data=param_data
            )
            data.append(processed_param)

        return Chart(
            title=title,
            chart_type=chart_type,
            data=data,
        )


chart_builder_dep = lambda: ChartBuilder()
