import json
from typing import List

from fastapi import APIRouter, Query, UploadFile, File, Depends

from src.models.schema.charts import Chart, ChartSchema
from src.service.pipe.impl.pandas_pipe import pandas_pipe, PandasPipe
from src.service.charts.impl.ai_chart_schema import AI_ChartSchema, ai_chart_schema
from src.service.charts.impl.chart_builder import ChartBuilder, chart_builder_dep

router = APIRouter(prefix="/charts", tags=["Charts"])


@router.post(
    path="/generate",
    description="Generar esquemas simples de gráficas"
)
async def generate_simple_schema(
        file: UploadFile = File(alias="file"),
        pipe: PandasPipe = Depends(pandas_pipe),
        charts: AI_ChartSchema = Depends(ai_chart_schema),
) -> List[ChartSchema]:
    df = await pipe.generate_df(file)
    columns = df.columns.tolist()
    dtypes = df.dtypes
    describe = df.describe()

    schema = charts.build_schema(columns, dtypes, describe)
    return schema


@router.post(path='/build', description="Construir gráficas")
async def build_chart(
        title: str = Query(description="titulo de la grafica"),
        chart_type: str = Query(description="tipo de gráfica"),
        parameter: str = Query(description="parámetros de la gráfica"),
        file: UploadFile = File(alias="file"),
        chart: ChartBuilder = Depends(chart_builder_dep),
) -> Chart:
    return await chart.build_chart(file, title, chart_type, parameter)
