from abc import ABC, abstractmethod
from typing import List
from src.models.schema.llm_schema import LLM_Message


class ABC_LLM(ABC):
    @abstractmethod
    def create(self, messages: List[LLM_Message]) -> str:
        raise NotImplementedError()
