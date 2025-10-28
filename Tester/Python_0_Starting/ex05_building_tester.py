from building import textStatistics

text1 = "Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
print("Test 1: Texte du sujet")
textStatistics(text1)
print()
print()
# Expected output pour Test 1:
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 7 punctuation marks
# 26 spaces
# 15 digits

text2 = "Hello World"
print("Test 2: Texte simple 'Hello World'")
textStatistics(text2)
print()
print()

text3 = "ABC abc 123 !@#"
print("Test 3: Texte 'ABC abc 123 !@#'")
textStatistics(text3)
print()
print()
