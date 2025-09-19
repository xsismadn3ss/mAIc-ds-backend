from fastapi import APIRouter, UploadFile, File, Depends

from src.service.pipe.impl.pandas_pipe_service import Pandas_Pipe_Service
from src.service.charts.impl.ai_chart_schema import AI_Chart_Schema


router = APIRouter(prefix="/upload", tags=["Upload"])


def pipe_service():
    return Pandas_Pipe_Service()


def chart_service():
    return AI_Chart_Schema()


@router.post("/", description="Enviar archivos CSV o excel para analizarlos con AI")
async def upload_file(
    file: UploadFile = File(...),
    pipe: Pandas_Pipe_Service = Depends(pipe_service),
    chart: AI_Chart_Schema = Depends(chart_service),
):
    df = await pipe.generate_df(file)

    columns = df.columns.to_list()
    dtypes = df.dtypes
    describe = df.describe()

    schema = chart.build_schemas(columns, dtypes, describe)
    return schema
