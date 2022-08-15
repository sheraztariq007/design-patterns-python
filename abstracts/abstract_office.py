from abc import ABC, abstractmethod

from abstracts.abstract_employee import AbstractEmployee


class AbstractOffice(ABC):

    @abstractmethod
    def create_ceo(self) -> AbstractEmployee:
        pass

    @abstractmethod
    def create_accountant(self) -> AbstractEmployee:
        pass


    # @abstractmethod
    # def create_product(self) -> List[AbstractProduct]:
    #     pass
    #
    # @abstractmethod
    # def create_departments(self) -> List[AbstractDepartment]:
    #     pass
