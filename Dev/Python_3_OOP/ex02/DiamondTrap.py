import sys as system
from pathlib import Path
system.path.insert(0, str(Path(__file__).parent.parent / "ex01"))
from S1E7 import Baratheon, Lannister  # noqa: E402


class King(Baratheon, Lannister):
    """Representing Kings of Westeros (Baratheon and Lannister)."""

    def __init__(self, first_name: str, is_alive: bool = True):
        '''King constructor method : \
King(first_name: str, is_alive: bool = True).'''
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        '''King method set_eyes(self, eyes: str) : sets eyes attribute.'''
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        '''King method set_hairs(self, hairs: str) : sets hairs attribute.'''
        self.hairs = hairs

    def get_eyes(self):
        '''King method get_eyes(self) : returns eyes attribute.'''
        return self.eyes

    def get_hairs(self):
        '''King method get_hairs(self) : returns hairs attribute.'''
        return self.hairs
