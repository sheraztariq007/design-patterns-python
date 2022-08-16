from dataclasses import dataclass
from typing import List

import dimensions
from window import Window


class Wall:

    def __init__(self, dims: dimensions.Dimensions):
        self.dimensions = dims
        self.windows: List[Window] = []

    def add_window(self, window):
        self.windows.append(window)
