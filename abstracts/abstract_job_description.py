from abc import ABC, abstractmethod
from typing import List


class AbstractJobDescription(ABC):

    @abstractmethod
    def __init__(self, name: str, responsibilities: List[str] = []):
        self._responsibilities = responsibilities
        self.name = name

    @abstractmethod
    def add_responsibility(self, responsibility):
        pass

    @abstractmethod
    def list_responsibilities(self) -> List[str]:
        pass
