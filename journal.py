import json
import logging
import os
from datetime import datetime
from os import PathLike
from typing import Optional

from helper.enum.atmosphere import Atmosphere
from planet import Planet


class Journal:
    def __init__(self, path: PathLike):
        self.entries = []
        self.planets = []
        self.invalid_bodies = [
            "Earthlike body",
            "Metal rich body"
        ]
        self.path = path
        self.logger = logging.getLogger('EDExo')

        odyssey_release_date = datetime(2021, 5, 19)

        journals = [os.path.join(path, file) for file in os.listdir(path)
                    if file.startswith("Journal.") and
                    os.path.getmtime(os.path.join(path, file)) > odyssey_release_date.timestamp()]

        for journal in journals:
            self.logger.info(f"Parsing {journal}")
            with open(journal, "r", encoding='utf-8') as file:
                lines = file.readlines()
                if json.loads(lines[0]).get("Odyssey"):
                    for line in lines:
                        self.parse(line)

        self.logger.info(f"Loaded {len(self.entries)} events")
        for entry in self.entries:
            self.parse_planet(entry)

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
            if "body" not in planet_class or planet_class in self.invalid_bodies:
                return
            atmosphere = event.get('Atmosphere')
            if not atmosphere:
                return
            atmosphere = Atmosphere(atmosphere)

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

    def parse(self, entry: str):
        entry = json.loads(entry)
        event = entry['event']

        # parsing bullshit
        # only add entry to journal iff it's either Scan or FSSBodySignals and the planet is not a star, belt, or ring
        if (
                ((event == 'Scan' and entry['ScanType'] == 'Detailed') or event == 'FSSBodySignals')
                and not entry.get('StarType')
                and all(x not in entry['BodyName'] for x in ["Belt Cluster", "Ring"])
        ):
            self.entries.append(entry)

    def watch(self):
        """
        Watches the journal for new events and parses them
        """
        pass
