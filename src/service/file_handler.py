from io import BytesIO
from fastapi import HTTPException, UploadFile
import pandas as pd


async def generate_df(file:UploadFile):
    if not file.filename or not file.filename.endswith((".csv", ".xlsx", ".xls")):
        raise HTTPException(406, "Formato no soportado")

    if file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)
    
    else:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents))

    return df