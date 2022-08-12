from abc import ABC, abstractmethod
from typing import List

from abstracts.AbstractDepartment import AbstractDepartment
from abstracts.AbstractProduct import AbstractProduct


class AbstractOffice(ABC):

    @abstractmethod
    def create_product(self) -> List[AbstractProduct]:
        pass

    @abstractmethod
    def create_departments(self) -> List[AbstractDepartment]:
        pass
