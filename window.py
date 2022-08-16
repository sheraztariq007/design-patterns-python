from abc import ABC
from dataclasses import dataclass

import dimensions


@dataclass(frozen=True)
class Window:
    dimensions: dimensions.Dimensions