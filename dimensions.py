from dataclasses import dataclass


@dataclass(frozen=True)
class Dimensions:
    Width: int
    Height: int
