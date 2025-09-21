import pandas as pd
from pandas import DataFrame
from fastapi import HTTPException, UploadFile
from ..abstract_pipe import ABC_Pipe
from typing import override


class PandasPipe(ABC_Pipe):
    @override
    async def generate_df(self, file: UploadFile) -> DataFrame:
        # validar si es un un archivo valido
        if not file.filename or not file.filename.endswith((".csv", ".xlsx", ".xls")):
            raise HTTPException(406, "Archivo no válido")

        # generar dataframe si es un CSV
        if file.filename.endswith(".csv"):
            df: DataFrame = pd.read_csv(filepath_or_buffer=file.file)

        # generar dataframe si es un excel
        else:
            df: DataFrame = pd.read_excel(file.file, engine='openpyxl')

        return df


def pandas_pipe():
    return PandasPipe()
