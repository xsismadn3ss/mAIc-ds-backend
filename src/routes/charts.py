from typing import List
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import json
from fastapi import APIRouter, Query, UploadFile, File, Depends, HTTPException

from src.models.schema.charts import ChartSchema, ChartReading, Chart
from src.models.schema.message import Message
from src.service.pipe.impl.pandas_pipe import pandas_pipe, PandasPipe
from src.service.charts.impl.ai_chart_schema import AI_ChartSchema, ai_chart_schema
from src.service.charts.impl.ai_chart_reader import AI_ChartReader, ai_chart_reader_dep
from src.service.charts.impl.chart_builder import ChartBuilder, chart_builder_dep

router = APIRouter(prefix="/charts", tags=["Charts"])


@router.post(path="/generate", description="Generar esquemas simples de gráficas")
async def generate_simple_schema(
    file: UploadFile = File(alias="file"),
    pipe: PandasPipe = Depends(pandas_pipe),
    charts: AI_ChartSchema = Depends(ai_chart_schema),
) -> List[ChartSchema]:
    df = await pipe.generate_df(file)
    columns = df.columns.tolist()
    dtypes = df.dtypes
    describe = df.describe()

    schema = await charts.build_schema(columns, dtypes, describe)
    return schema


@router.post(path="/build", description="Construir gráficas")
async def build_chart(
    charts_schema: str = Query(description="Esquemas de gráficas"),
    file: UploadFile = File(...),
    chart_builder: ChartBuilder = Depends(chart_builder_dep),
    pandas_pipe: PandasPipe = Depends(pandas_pipe),
) -> List[Chart]:
    try:
        data: dict = json.loads(charts_schema)
        schemas = [ChartSchema(**d) for d in data]

        df = await pandas_pipe.generate_df(file)

        charts: List[Chart] = []
        for schema in schemas:
            chart = chart_builder.build_chart(
                df, schema.title, schema.chart_type, schema.parameter, schema.mesure
            )
            charts.append(chart)
        return charts

    except json.JSONDecodeError as e:
        print(str(e))
        raise HTTPException(
            status_code=400,
            detail="Error al decodificar el JSON de los esquemas de gráficas",
        )
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.post(path="/read", description="Leer gráficas")
async def read_chart(
    charts: ChartReading,
    chart_reader: AI_ChartReader = Depends(ai_chart_reader_dep),
):
    return Message(message=await chart_reader.read_charts(charts.charts))
