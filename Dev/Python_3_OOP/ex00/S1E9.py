from abc import ABC, abstractmethod


class Character(ABC):
    """Character Class is an abstract base class for all characters."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        '''Character abstract constructor method : \
Character(first_name: str, is_alive: bool = True).'''
        ...  # To be implemented in the subclass.

    @abstractmethod
    def die(self) -> None:
        '''Character abstract method Die(self).'''
        ...  # To be implemented in the subclass.


class Stark(Character):
    """Stark Class is a subclass of Character for the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        '''Stark constructor method : \
Stark(first_name: str, is_alive: bool = True).'''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        '''Stark method die(self) : \
sets the is_alive attribute to False.'''
        self.is_alive = False
