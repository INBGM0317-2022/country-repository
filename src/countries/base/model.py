from __future__ import annotations

from dataclasses import field, dataclass
from enum import Enum


@dataclass
class Country:
    """
    Represents a country.
    """

    name: str = field()
    """name of the country"""
    population: int = field()
    """population of the country"""
    translations: dict[str, str] = field()
    """translations of the name"""
    timezones: list[str] = field()
    """timezones of the country"""
    independent: bool = field()
    """whether the country is independent or not"""
    area: int = field(default=None)
    """area of the country"""
    capital: str = field(default=None)
    """capital of the country"""
    region: Region = field(default=None)
    """region of the country"""
    code: str = field(default=None)
    """code of the country"""

    class Region(Enum):
        """
        Represents regions.

        * AFRICA = "Africa"
        * AMERICAS = "Americas"
        * ANTARCTIC = "Antarctic"
        * ANTARCTIC_OCEAN = "Antarctic Ocean"
        * ASIA = "Asia"
        * EUROPE = "Europe"
        * OCEANIA = "Oceania"
        * POLAR = "Polar"
        """
        AFRICA = "Africa"
        AMERICAS = "Americas"
        ANTARCTIC = "Antarctic"
        ANTARCTIC_OCEAN = "Antarctic Ocean"
        ASIA = "Asia"
        EUROPE = "Europe"
        OCEANIA = "Oceania"
        POLAR = "Polar"
