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
        self.distance = distance
        self.atmosphere = atmosphere
        self.volcanism = volcanism
        self.gravity = gravity
        self.temperature = temperature
        self.signals = signals

        if planet_class and "body" in planet_class:
            self.cls: PlanetClass = PlanetClass(planet_class)
        else:
            self.cls = PlanetClass.INVALID

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if key == 'planet_class':
                self.cls = PlanetClass(value)
            else:
                setattr(self, key, value)

    def __str__(self) -> str:
        return f"""name: {self.name} system_name: {self.system_name} distance: {self.distance} cls: {self.cls} atmosphere: {self.atmosphere} volcanism: {self.volcanism} gravity: {self.gravity} temperature: {self.temperature} signals: {self.signals}"""
