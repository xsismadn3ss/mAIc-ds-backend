from typing import Any, List
from pydantic import BaseModel, Field


class ChartParameter(BaseModel):
    x_axis: str = Field(description="Eje X")
    y_axis: str = Field(description="Eje Y")

class DataValue(BaseModel):
    x: Any
    y: Any

class ParameterProccesed(BaseModel):
    x_axis: str
    y_axis: str
    data: List[DataValue]


class ChartScheme(BaseModel):
    title: str = Field("Titulo de la gráfica")
    chart_type: str = Field("Tipo de gráfica")
    data: List[ParameterProccesed]

