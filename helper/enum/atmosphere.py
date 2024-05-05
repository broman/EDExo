from enum import Enum


def parse_atmosphere(atmo: str):
    _type = AtmosphereType.AMMONIA
    volume = AtmosphereVolume.NORMAL
    density = AtmosphereDensity.NORMAL

    atmo = atmo.lower().replace("atmosphere", '').replace("hot", '')
    if "thick" in atmo:
        atmo = atmo.replace("thick", '')
        volume = AtmosphereVolume.THICK
    elif "thin" in atmo:
        atmo = atmo.replace("thin", '')
        volume = AtmosphereVolume.THIN

    if "rich" in atmo:
        atmo = atmo.replace("rich", '')
        density = AtmosphereDensity.RICH

    _type = AtmosphereType(atmo.strip())

    return _type, volume, density


class Atmosphere:
    def __init__(self, atmosphere: str):
        self.atmosphere = atmosphere
        (
            self.atmosphere_type,
            self.atmosphere_volume,
            self.atmosphere_density
        ) = parse_atmosphere(atmosphere)


class AtmosphereType(Enum):
    AMMONIA = "ammonia"
    ARGON = "argon"
    METHANE = "methane"
    HELIUM = "helium"
    NEON = "neon"
    NITROGEN = "nitrogen"
    OXYGEN = "oxygen"
    CARBON_DIOXIDE = "carbon dioxide"
    WATER = "water"
    SULFUR_DIOXIDE = "sulfur dioxide"


class AtmosphereVolume(Enum):
    THIN = 1
    NORMAL = 2
    THICK = 3


class AtmosphereDensity(Enum):
    NORMAL = 1
    RICH = 2
