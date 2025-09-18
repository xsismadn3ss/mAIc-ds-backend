import json
from fastapi import APIRouter, Query, UploadFile, File

from src.models.schema.charts import ChartParameter, ChartScheme
from src.service.chart_builder import handle_parameters
from src.service.file_handler import generate_df

router = APIRouter(prefix="/charts", tags=["Charts"])

@router.post(
    path='/build',
    description="Construir gráfica a partir de un esquema"
)
async def build(
    title:str = Query(description="titulo de la grafica"),
    chart_type:str = Query(description="tipo de gráfica"),
    parameter: str = Query(description="Parametros de la gráfica"),
    file: UploadFile = File(...),
):
    # convertir parameter a un Schema
    data = json.loads(parameter)
    p = [ChartParameter(**d) for d in  data]

    # validar archivo
    df = generate_df(file)

    # generar datos a partir de los parametros otorgados
    processed_parameters = handle_parameters(p, df)
    
    # Crear el esquema de la gráfica
    chart_scheme = ChartScheme(
        title=title,
        chart_type=chart_type,
        data=processed_parameters
    )
    
    return chart_scheme.model_dump()