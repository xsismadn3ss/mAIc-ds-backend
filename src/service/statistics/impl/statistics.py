from typing import Any

from pandas import DataFrame
from typing_extensions import override

from ..abc_statistics import ABCStatistics


class Statistics(ABCStatistics):
    def __init__(self):
        self.statistics = {}

    @override
    def mean(self, column: str, df: DataFrame) -> Any:
        return df.mean()[column]

    @override
    def median(self, column: str, df: DataFrame) -> Any:
        return df.median()[column]

    @override
    def mode(self, column: str, df: DataFrame) -> Any:
        return df.mode()[column]

    @override
    def std(self, column: str, df: DataFrame) -> Any:
        return df.std()[column]


statistics_dep = lambda: Statistics()
