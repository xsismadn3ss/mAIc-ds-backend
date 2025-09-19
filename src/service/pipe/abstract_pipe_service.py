from abc import ABC, abstractmethod
from pandas import DataFrame
from fastapi import UploadFile

class Abstract_Pipe_Service(ABC):
    @abstractmethod
    async def generate_df(self, file: UploadFile) -> DataFrame:
        raise NotImplementedError()