from abc import abstractmethod, ABC
from typing import List

from abstracts.abstract_job_description import AbstractJobDescription


class AbstractEmployee(ABC):

    @abstractmethod
    def __init__(self, name:str, address:str, hobbies:List[str], responsibilities:List[str]):
        self.name = name
        self.address = address
        self.hobbies = hobbies
        self.responsibilities = responsibilities

    @abstractmethod
    def get_job_description(self) -> AbstractJobDescription:
        pass
