import sys as system
from pathlib import Path
system.path.insert(0, str(Path(__file__).parent.parent / "ex00"))
from S1E9 import Character  # noqa: E402


class Baratheon(Character):
    """Representing the Baratheon family."""
    VECTOR = ('Baratheon', 'brown', 'dark')

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Baratheon constructor method : \
Baratheon(first_name: str, is_alive: bool = True).'''
        super().__init__(first_name, is_alive)
        self.family_name = self.VECTOR[0]
        self.eyes = self.VECTOR[1]
        self.hairs = self.VECTOR[2]

    def __str__(self):
        '''Baratheon method __str__(self) : \
returns the string representation of the Baratheon character.'''
        return f"Vector: {self.VECTOR}"

    def __repr__(self):
        '''Baratheon method __repr__(self) : \
returns the string representation of the Baratheon character.'''
        return f"Vector: {self.VECTOR}"


class Lannister(Character):
    """Representing the Lannister family."""
    VECTOR = ('Lannister', 'blue', 'light')

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Lannister constructor method : \
Lannister(first_name: str, is_alive: bool = True).'''
        super().__init__(first_name, is_alive)
        self.family_name = self.VECTOR[0]
        self.eyes = self.VECTOR[1]
        self.hairs = self.VECTOR[2]

    def __str__(self):
        '''Lannister method __str__(self) : \
returns the string representation of the Lannister character.'''
        return f"Vector: {self.VECTOR}"

    def __repr__(self):
        '''Lannister method __repr__(self) : \
returns the string representation of the Lannister character.'''
        return f"Vector: {self.VECTOR}"

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        '''Lannister method create_lannister(first_name, is_alive= True) : \
creates a new Lannister character.'''
        return Lannister(first_name, is_alive)