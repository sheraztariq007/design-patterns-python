from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @abstractmethod
    def set_price(self, price:int):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_name(self):
        pass
