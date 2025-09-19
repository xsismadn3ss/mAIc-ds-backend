from abc import abstractmethod, ABC
from typing import Dict

class ABC_Chart_Schema(ABC):
    @abstractmethod
    def build_schemas(self, columns, dtypes, describe) -> Dict[str, object]:
        raise NotImplementedError()