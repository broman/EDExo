import logging

from helper.enum.planetclass import PlanetClass, get_class


class Planet:
    def __init__(
            self,
            name: str,
            system_name: str = None,
            distance: float = None,
            planet_class: str = None,
            atmosphere: str = None,
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

        self.cls: PlanetClass = get_class(planet_class)

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if key == 'planet_class':
                self.cls = get_class(value)
            else:
                setattr(self, key, value)

    def __str__(self) -> str:
        return f"""name: {self.name} system_name: {self.system_name} distance: {self.distance} cls: {self.cls} atmosphere: {self.atmosphere} volcanism: {self.volcanism} gravity: {self.gravity} temperature: {self.temperature} signals: {self.signals}"""
