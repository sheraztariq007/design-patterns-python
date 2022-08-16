from abc import ABC, abstractmethod

from house import House
from roof import Roof
from room import Room
from wall import Wall
from window import Window


class Builder(ABC):

    @property
    @abstractmethod
    def house(self) -> House:
        pass

    @abstractmethod
    def add_room(self, room: Room) -> None:
        pass

    @abstractmethod
    def add_roof(self, roof: Roof) -> None:
        pass


class ConcreteBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    @property
    def house(self) -> House:
        house = self._house
        self.reset()
        return house

    def add_room(self, room: Room) -> None:
        self._house.add_room(room=room)

    def add_roof(self, roof: Roof) -> None:
        self._house.add_roof(roof=roof)
