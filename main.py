import logging
import json
import os
from pathlib import Path

from journal import Journal


class EDExo:
    def __init__(self):
        self.logger = logging.getLogger('EDExo')
        logging.basicConfig(level=logging.INFO)
        self.logger.info("Reading settings from file")

        self.path = json.load(open('settings.json'))
        self.path = Path(self.path['journal_file_path'].replace("%userprofile%", os.environ['USERPROFILE']))
        self.logger.info(f"Journal path: {self.path}")
        if not self.path:
            logging.error(f'No journal file found in {self.path}')
            raise FileNotFoundError("No journal file found")

        self.logger.info("Initializing EDExo")
        self.journal = Journal(self.path)


if __name__ == '__main__':
    EDExo()
