import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "ex00"))
from S1E9 import Character  # noqa: E402


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Baratheon constructor method : \
Baratheon(first_name: str, is_alive: bool = True).'''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = __class__.__name__
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        '''Baratheon method die(self) : \
sets the is_alive attribute to False.'''
        self.is_alive = False

    def __str__(self):
        '''Baratheon method __str__(self) : \
returns the string representation of the Baratheon character.'''
        self.vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {self.vector}"

    def __repr__(self):
        '''Baratheon method __repr__(self) : \
returns the string representation of the Baratheon character.'''
        self.vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {self.vector}"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Lannister constructor method : \
Lannister(first_name: str, is_alive: bool = True).'''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = __class__.__name__
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        '''Lannister method die(self) : \
sets the is_alive attribute to False.'''
        self.is_alive = False

    def __str__(self):
        '''Lannister method __str__(self) : \
returns the string representation of the Lannister character.'''
        self.vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {self.vector}"

    def __repr__(self):
        '''Lannister method __repr__(self) : \
returns the string representation of the Lannister character.'''
        self.vector = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {self.vector}"

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        '''Lannister method create_lannister(first_name: str, is_alive: bool = True) : \
creates a new Lannister character.'''
        return Lannister(first_name, is_alive)
