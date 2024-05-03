import json
import logging
import os
from datetime import datetime
from os import PathLike


class Journal:
    def __init__(self, path: PathLike):
        self.entries = []
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
