from math import ceil, floor


def ceiling(x: float, factor: int = 1) -> float:
    return ceil(x * factor) / factor


def flooring(x: float, factor: int = 1) -> float:
    return floor(x * factor) / factor
