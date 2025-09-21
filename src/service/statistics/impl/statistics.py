from typing import Any

import re
from pandas import DataFrame, Series
from typing import override, Optional

from src.enums.statistics_enum import Mesures
from src.service.statistics.abc_statistics import ABCStatistics


def remove_parentheses_content(text):
    """
    Elimina el contenido encerrado en paréntesis (incluyendo los paréntesis)
    y cualquier espacio en blanco que lo preceda.

    Args:
        text (str): El texto de entrada.

    Returns:
        str: El texto modificado sin el contenido entre paréntesis.
    """
    return re.sub(r"\s*\(.*?\)", "", text).strip()


class Statistics(ABCStatistics):
    @override
    def mean(self, x_column: str | None, y_column: str, df: DataFrame) -> Any:
        if x_column:
            return df.groupby(x_column)[y_column].mean()
        return df[y_column].mean()

    @override
    def median(self, x_column: str | None, y_column: str, df: DataFrame) -> Any:
        if x_column:
            return df.groupby(x_column)[y_column].median()
        return df[y_column].median()

    @override
    def mode(self, x_column: str | None, y_column: str, df: DataFrame) -> Any:
        if x_column:
            return df.groupby(x_column)[y_column].apply(
                lambda x: x.mode().iloc[0] if not x.mode().empty else None
            )
        return df[y_column].mode().iloc[0] if not df[y_column].mode().empty else None

    @override
    def std(self, x_column: str | None, y_column: str, df: DataFrame) -> Any:
        if x_column:
            return df.groupby(x_column)[y_column].std()
        return df[y_column].std()

    def handle(self, x_column: str | None, y_column: str, mesure: str, df: DataFrame):
        clean_y_column = remove_parentheses_content(y_column)
        if Mesures.MEDIANA.value in mesure:
            return self.median(x_column, clean_y_column, df)
        elif Mesures.PROMEDIO.value in mesure:
            return self.mean(x_column, clean_y_column, df)
        elif Mesures.DIST_ESTAND.value in mesure:
            return self.std(x_column, clean_y_column, df)
        elif Mesures.DESV_ESTAND.value in mesure:
            return self.std(x_column, clean_y_column, df)
        else:
            # devolver serie normal en base x y y
            if x_column:
                return df.groupby(x_column)[clean_y_column].apply(lambda x: x)
            return df[clean_y_column]


def statistics_dep():
    return Statistics()
