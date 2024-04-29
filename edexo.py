import logging
import json
import os
from pathlib import Path

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

        for event in self.journal.fss_scans:
            self.logger.info(event)
            self.parse_planet(event)

        for event in self.journal.detailed_scans:
            self.logger.info(event)
            self.parse_planet(event)

    def parse_planet(self, event: dict):
        #TODO
        planet = None
        if event['event'] == 'FSSBodySignals':
            pass
        if event['BodyName'] not in [x.name for x in self.planets]:
            planet = Planet(name=event['BodyName'])
            self.planets.append(planet)
        if event.get('Signals'):
            signals = [x['Count'] for x in event['Signals'] if x['Type_Localised'] == 'Biological'][0]


if __name__ == '__main__':
    logger = logging.getLogger("EDExo")
    logging.basicConfig(level=logging.INFO)
    logger.info("Initializing EDExo")
    ede = EDExo()
