import re
from typing import List

import pandas as pd
from pandas import DataFrame

from src.models.schema.charts import ChartParameter, ParameterProccesed, DataValue
from src.service.statistics.impl.statistics import Statistics


class ChartDataProcessor:
    def __init__(self, statistics: Statistics):
        self.statistics = statistics

    def _clean_axis_name(self, value: str) -> str:
        return re.sub(r"\s*\(.*\)", "", value).strip()

    def _process_result(
        self, x_axis: str, y_axis: str, result: pd.Series | float
    ) -> List[ParameterProccesed]:
        if isinstance(result, pd.Series):
            list_of_data_values = [
                DataValue(x=idx[0] if isinstance(idx, (tuple, list)) else idx, y=val)
                for idx, val in result.items()
            ]
            return [
                ParameterProccesed(
                    x_axis=x_axis, y_axis=y_axis, data=list_of_data_values
                )
            ]
        else:
            return [
                ParameterProccesed(
                    x_axis=x_axis, y_axis=y_axis, data=[DataValue(x=None, y=result)]
                )
            ]

    def process_parameters(
        self, df: DataFrame, parameters: List[ChartParameter], mesure: str
    ) -> List[ParameterProccesed]:
        data_processed = []
        for param in parameters:
            x_axis_raw = param.x_axis
            y_axis_raw = param.y_axis

            x_axis = self._clean_axis_name(x_axis_raw) if x_axis_raw else None
            y_axis = self._clean_axis_name(y_axis_raw)

            if y_axis not in df.columns:
                print(
                    f"Advertencia: La columna {y_axis} no se encontró en el DataFrame."
                )
                continue

            if x_axis and x_axis not in df.columns:
                raise ValueError(f"Columna {x_axis} no existe")

            if x_axis and x_axis in df.columns:
                result = self.statistics.handle(x_axis, y_axis, mesure, df)
                processed_data = self._process_result(x_axis, y_axis, result)
            else:
                result = self.statistics.handle(None, y_axis, df)
                processed_data = self._process_result(None, y_axis, result)

            data_processed.extend(processed_data)
        return data_processed
