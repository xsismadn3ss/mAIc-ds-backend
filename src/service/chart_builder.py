from typing import List

from fastapi import HTTPException
from pandas import DataFrame

from src.models.schema.charts import ChartParameter, DataValue, ParameterProccesed


def handle_parameters(parameter: List[ChartParameter], df: DataFrame):
    processed_parameters = []

    for param in parameter:
        # Verificar que las columnas existen en el DataFrame
        if param.x_axis not in df.columns:
            raise HTTPException(400, f"La columna '{param.x_axis}' no existe en el archivo")
        if param.y_axis not in df.columns:
            raise HTTPException(400, f"La columna '{param.y_axis}' no existe en el archivo")
        
        # Extraer datos de las columnas especificadas para este parámetro
        param_data = []
        for _, row in df.iterrows():
            param_data.append(DataValue(
                x=row[param.x_axis],
                y=row[param.y_axis]
            ))
        
        # Crear el parámetro procesado con sus datos
        processed_param = ParameterProccesed(
            x_axis=param.x_axis,
            y_axis=param.y_axis,
            data=param_data
        )
        processed_parameters.append(processed_param)

    return processed_parameters