from typing import List

from helper.spawnparameter import SpawnParameter


class Specimen:
    def __init__(
        self,
        genus: str,
        species: str,
        value: int,
        params: [SpawnParameter]
    ):
        self.genus = genus
        self.species = species
        self.value = value
        self.params = params
