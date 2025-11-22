import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Returns a random ID.'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Student dataclass.'''
    name: str = field(default="unknown_name")
    surname: str = field(default="unknown_surname")
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = f"{self.name.lower()}.{self.surname.lower()}"
        self.id = generate_id()
