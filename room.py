from typing import List

from wall import Wall


class Room:

    def __init__(self, ):
        self.walls: List[Wall] = []

    def add_wall(self, wall: Wall):
        self.walls.append(wall)
