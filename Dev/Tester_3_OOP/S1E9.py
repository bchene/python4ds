from abc import ABC, abstractmethod


class Character(ABC):
    """Character Class is an abstract base class for all characters."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        '''Character abstract constructor method : \
Character(first_name: str, is_alive: bool = True).'''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        '''Character method Die(self). \
Sets the is_alive attribute to False.'''
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Stark constructor method : \
Stark(first_name: str, is_alive: bool = True).'''
        super().__init__(first_name, is_alive)
