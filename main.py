from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from builder import ConcreteBuilder
from dimensions import Dimensions
from roof import Roof

if __name__ == "__main__":
    builder = ConcreteBuilder()

    roof_dims = Dimensions(20, 30)

    roof = Roof(dims=roof_dims)

    builder.add_roof(roof=roof)

    house = builder.house

    print(house)
