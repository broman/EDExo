import logging

from helper.enum.atmosphere import Atmosphere
from helper.enum.planetclass import PlanetClass


class Planet:
    def __init__(
            self,
            name: str,
            system_name: str = None,
            distance: float = None,
            planet_class: str = None,
            atmosphere: Atmosphere = None,
            volcanism: str = None,
            gravity: float = None,
            temperature: int = None,
            signals: int = None,
    ):
        self.name = name
        self.system_name = system_name
        self.cls = None
        self.distance = distance
        self.atmosphere = atmosphere
        self.volcanism = volcanism
        self.gravity = gravity
        self.temperature = temperature
        self.signals = signals

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if key == 'planet_class':
                self.cls = PlanetClass(value)
            else:
                setattr(self, key, value)

    def __str__(self) -> str:
        return str({k: str(v) if hasattr(v, "__dict__") else v for k, v in vars(self).items()})
