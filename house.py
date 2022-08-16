from dataclasses import dataclass
from typing import List

from roof import Roof
from room import Room

@dataclass
class House:
    def __init__(self):
        self._roof = None
        self._rooms: List[Room] = []
        self._roof: Roof

    def add_room(self, room: Room):
        self._rooms.append(room)

    def add_roof(self, roof: Roof):
        self._roof = roof

    def __repr__(self):
        print(f'Roof: {self._roof} , Rooms: {self._rooms}')

    def __str__(self):
        return f'Roof: {self._roof} , Rooms: {self._rooms}'

