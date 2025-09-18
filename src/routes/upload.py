from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse

from src.service.ai_data_science import analyze_df
from src.service.file_handler import generate_df


router = APIRouter(prefix='/upload', tags=["Upload"])

@router.post(
    '/',
    description="Enviar archivos CSV o excel para analizarlos con AI")
async def upload_file(file: UploadFile = File(...)):
    df = generate_df(file)

    # context
    columns = df.columns.tolist()
    dtypes = df.dtypes
    describe = df.describe()

    return StreamingResponse(analyze_df(columns, dtypes, describe), media_type="text/plain")
