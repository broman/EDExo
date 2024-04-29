import json
import logging
import os
from os import PathLike


class Journal:
    def __init__(self, path: PathLike):
        self.fss_scans = []
        self.detailed_scans = []
        self.path = path
        self.logger = logging.getLogger('EDExo')

        journals = [os.path.join(path, file) for file in [f for f in os.listdir(path) if f.startswith("Journal.")]]
        self.journal = max(journals, key=os.path.getmtime)
        self.logger.info(f"Selected most recently modified journal {self.journal}")
        for line in open(self.journal, "rb").readlines():
            self.parse(line)

        self.logger.info(f"Loaded {len(self.detailed_scans) + len(self.fss_scans)} events from {self.journal}")

    def parse(self, entry: bytes):
        loaded = json.loads(entry)
        if loaded['event'] == "FSSBodySignals":
            self.fss_scans.append(loaded)
        elif loaded['event'] == "Scan" and loaded['ScanType'] == "Detailed":
            self.detailed_scans.append(loaded)

    def watch(self):
        """
        Watches the journal for new events and parses them
        """
        pass
