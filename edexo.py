import json
import logging
import os
from pathlib import Path

from journal import Journal


class EDExo:
    def __init__(self):
        # locate most recent journal file and parse it
        self.planets = []
        self.logger = logging.getLogger('EDExo')
        self.logger.info("Reading settings from file")
        self.path = json.load(open('settings.json'))
        self.path = Path(self.path['journal_file_path'].replace("%userprofile%", os.environ['USERPROFILE']))
        self.logger.info(f"Journal located: {self.path}")
        if not self.path:
            logging.error(f'No journal file found in {self.path}')
            raise FileNotFoundError("No journal file found")
        self.journal = Journal(self.path, self.on_new_event)
        self.planets = self.journal.planets
        [self.logger.info(x) for x in self.planets]

    def on_new_event(self):
        self.planets = self.journal.planets


if __name__ == '__main__':
    logger = logging.getLogger("EDExo")
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Initializing EDExo")
    ede = EDExo()
