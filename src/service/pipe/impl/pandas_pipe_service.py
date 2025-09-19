import pandas as pd
from pandas import DataFrame
from io import BytesIO
from fastapi import HTTPException, UploadFile
from ..abstract_pipe_service import Abstract_Pipe_Service
from typing import override

class Pandas_Pipe_Service(Abstract_Pipe_Service):
    @override
    async def generate_df(self, file: UploadFile) -> DataFrame:
        # validar si es un un archivo valido
        if not file.filename or not file.filename.endswith((".csv", ".xlsx", ".xls")):
            raise HTTPException(406, "Archivo no válido")
        
        # generar dataframe si es un CSV
        if file.filename.endswith(".csv"):
            df : DataFrame = pd.read_csv(filepath_or_buffer=file.file)
        
        # generar dataframe si es un excel
        else:
            content: bytes = await file.read()
            df: DataFrame = pd.read_excel(BytesIO(initial_bytes=content))
        
        return df