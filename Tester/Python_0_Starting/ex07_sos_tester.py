from sos import textToMorseString

print("Test 1: 'HELLO'")
print(textToMorseString("HELLO"))
# .... . .-.. .-.. ---
print()

print("Test 2: 'HELLO WORLD'")
print(textToMorseString("HELLO WORLD"))
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
print()

print("Test 3: 'SOS'")
print(textToMorseString("SOS"))
# ... --- ...
print()
