from abc import abstractmethod, ABC
from typing import List

from src.models.schema.charts import ChartSchema


class ABC_ChartSchema(ABC):
    @abstractmethod
    async def build_schema(self, columns, dtypes, describe) -> List[ChartSchema]:
        raise NotImplementedError()
