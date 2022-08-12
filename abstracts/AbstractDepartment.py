from abc import abstractmethod, ABC


class AbstractDepartment(ABC):

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
