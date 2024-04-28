from helper.enum.planetclass import PlanetClass


class Planet:
    def __init__(
        self,
        name: str,
        distance: float,
        cls: PlanetClass,
        atmosphere: str,
        volcanism: str,
        gravity: float,
        temperature: int
    ):
        self.name = name
        self.distance = distance
        self.cls = cls
        self.atmosphere = atmosphere
        self.volcanism = volcanism
        self.gravity = gravity
        self.temperature = temperature

