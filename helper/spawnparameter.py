from helper.enum.atmosphere import Atmosphere


class SpawnParameter:
    def __init__(
        self,
        atmosphere: Atmosphere = None,
        body_type: str = None,
        gravity_max: float = None,
        gravity_min: float = None,
        temp_max: float = None,
        temp_min: float = None,
    ):
        self.atmosphere = atmosphere
        self.body_type = body_type
        self.gravity_max = gravity_max
        self.gravity_min = gravity_min
        self.temp_max = temp_max
        self.temp_min = temp_min

