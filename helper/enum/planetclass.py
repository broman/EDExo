from enum import Enum


class PlanetClass(Enum):
    HIGH_METAL_CONTENT = "High metal content body"
    ROCKY = "Rocky body"
    ICY = "Icy body"
    ROCKY_ICY = "Rocky ice body"
    INVALID = 5
