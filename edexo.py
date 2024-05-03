import logging
import json
import os
from pathlib import Path
from typing import Optional

from journal import Journal
from planet import Planet


class EDExo:
    def __init__(self):
        self.planets: [Planet] = []

        # locate most recent journal file and parse it
        self.logger = logging.getLogger('EDExo')
        self.logger.info("Reading settings from file")
        self.path = json.load(open('settings.json'))
        self.path = Path(self.path['journal_file_path'].replace("%userprofile%", os.environ['USERPROFILE']))
        self.logger.info(f"Journal located: {self.path}")
        if not self.path:
            logging.error(f'No journal file found in {self.path}')
            raise FileNotFoundError("No journal file found")
        self.journal = Journal(self.path)

        for event in self.journal.entries:
            self.parse_planet(event)

        [self.logger.info(x) for x in self.planets]

    def parse_planet(self, event: dict):
        name: str = event['BodyName']

        if event['event'] == 'FSSBodySignals':
            # Maps
            signal_count = 0
            if signals := event.get("Signals"):
                for signal in signals:
                    if signal['Type_Localised'] == 'Biological':
                        signal_count = signal['Count']
            self.add_planet(planet=name, signals=signal_count)

        else:
            # FSS scans
            system_name = event['StarSystem']
            distance = event['DistanceFromArrivalLS']
            planet_class = event['PlanetClass']
            atmosphere = event.get('Atmosphere')
            atmosphere_type = event.get('AtmosphereType')
            atmosphere_composition = event.get('Atmosphere_Type')

            volcanism = event['Volcanism']
            gravity = event['SurfaceGravity']
            surface_temperature = event['SurfaceTemperature']

            self.add_planet(
                planet=name,
                system_name=system_name,
                distance=distance,
                planet_class=planet_class,
                atmosphere=atmosphere,
                atmosphere_type=atmosphere_type,
                atmosphere_composition=atmosphere_composition,
                volcanism=volcanism,
                gravity=gravity,
                temperature=surface_temperature,
            )

    def add_planet(self, planet: str, **kwargs):
        if _planet := self.get_planet_by_name(planet):
            _planet.update(**kwargs)
        else:
            _planet = Planet(name=planet)
            _planet.update(**kwargs)
            self.planets.append(_planet)

    def get_planet_by_name(self, name: str) -> Optional[Planet]:
        return next(filter(lambda x: x.name == name, self.planets), None)


if __name__ == '__main__':
    logger = logging.getLogger("EDExo")
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Initializing EDExo")
    ede = EDExo()
