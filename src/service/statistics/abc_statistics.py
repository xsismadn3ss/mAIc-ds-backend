from abc import ABC, abstractmethod
from typing import Any

from pandas import DataFrame


class ABCStatistics(ABC):
    @abstractmethod
    def mean(self, column: str, df: DataFrame) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def median(self, column: str, df: DataFrame) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def mode(self, column: str, df: DataFrame) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def std(self, column: str, df: DataFrame) -> Any:
        raise NotImplementedError()
