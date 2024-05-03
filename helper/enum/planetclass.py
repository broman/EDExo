from enum import Enum


def get_class(name: str):
    match name:
        case "High metal content body":
            return PlanetClass.HIGH_METAL_CONTENT
        case "Rocky body":
            return PlanetClass.ROCKY
        case "Icy body":
            return PlanetClass.ICY
        case "Rocky ice body":
            return PlanetClass.ROCKY_ICY


class PlanetClass(Enum):
    HIGH_METAL_CONTENT = 1
    ROCKY = 2
    ICY = 3
    ROCKY_ICY = 4
