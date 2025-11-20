# Tester du sujet
from S1E9 import Character, Stark

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)

print("\n---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

print("\n---")
try:
    hodor = Character("hodor")
except TypeError as e:
    print("\033[91mTypeError: " + str(e) + "\033[0m")

# Expected output:
# ------------------------------------------------------------
# {'first_name': 'Ned', 'is_alive': True}
# True
# False
# Your docstring for Class
# Your docstring for Constructor
# Your docstring for Method
#
# ---
# {'first_name': 'Lyanna', 'is_alive': False}
#
# ---
# Can't instantiate abstract class Character with abstract methods __init__, die
#
# ------------------------------------------------------------
