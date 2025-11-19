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

# Ned = Stark("Ned")
# >
# print(Ned.__dict__)
# > {'first_name': 'Ned', 'is_alive': True}
# print(Ned.is_alive)
# > True
# Ned.die()
# >
# print(Ned.is_alive)
# > False
# print(Ned.__doc__)
# > Stark Class is a subclass of Character for the Stark family.
# print(Ned.__init__.__doc__)
# > Constructor Method Stark(first_name: str, is_alive: bool = True).
# print(Ned.die.__doc__)
# > Stark method die(self) : sets the is_alive attribute to False.
# print("---")
# > ---
# Lyanna = Stark("Lyanna", False)
# >
# print(Lyanna.__dict__)
# > {'first_name': 'Lyanna', 'is_alive': False}
