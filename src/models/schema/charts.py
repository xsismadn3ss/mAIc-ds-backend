"""Esquemas de datos para gráficas"""

from typing import Any, List, Optional
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


class ChartSchema(BaseModel):
    title: str = Field(description="Titulo de la  gráfica")
    chart_type: str = Field(description="Tipo de gráfica")
    mesure: str = Field(description="Métrica a utilizar")
    parameter: List[ChartParameter] = Field(description="Parámetros")


class Chart(BaseModel):
    title: str = Field(description="Titulo de la gráfica")
    chart_type: str = Field(description="Tipo de gráfica")
    data: Optional[List[ParameterProccesed]] = Field(description="Datos procesados")


class ChartReading(BaseModel):
    charts: List[Chart] = Field(description="Gráficas")
