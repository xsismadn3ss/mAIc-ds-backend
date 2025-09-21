from abc import ABC, abstractmethod
from typing import Any

from pandas import DataFrame


class ABCStatistics(ABC):
    @abstractmethod
    def mean(self, x_column: str | None, y_column: str, df: DataFrame) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def median(self, x_column: str | None, y_column: str, df: DataFrame) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def mode(self, x_column: str | None, y_column: str, df: DataFrame) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def std(self, x_column: str | None, y_column: str, df: DataFrame) -> Any:
        raise NotImplementedError()
