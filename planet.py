from helper.enum.planetclass import PlanetClass


class Planet:
    def __init__(
        self,
        name: str,
        system_name: str = None,
        distance: float = None,
        cls: PlanetClass = None,
        atmosphere: str = None,
        volcanism: str = None,
        gravity: float = None,
        temperature: int = None,
        signals: int = None,
    ):
        self.name = name
        self.system_name = system_name
        self.distance = distance
        self.cls = cls
        self.atmosphere = atmosphere
        self.volcanism = volcanism
        self.gravity = gravity
        self.temperature = temperature
        self.signals = signals

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

