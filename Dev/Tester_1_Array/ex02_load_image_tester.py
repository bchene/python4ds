from load_image import ft_load


print("\033[2;34mTEST 1 : ft_load('landscape.jpg'):\033[0m")
try:
    print(ft_load("landscape.jpg"))
except Exception as e:
    print(f"\033[91mAssertionError: {e}\033[0m")
print()

print("\033[2;34mTEST 2 : ft_load('nofile'):\033[0m")
try:
    print(ft_load("nofile"))
except Exception as e:
    print(f"\033[91mAssertionError: {e}\033[0m")
print()

print("\033[2;34mTEST 3 : ft_load('ex02_load_image_tester.py'):\033[0m")
try:
    print(ft_load("ex02_load_image_tester.py"))
except Exception as e:
    print(f"\033[91mAssertionError: {e}\033[0m")
print()

print("\033[2;34mTEST 4 : ft_load('landscape_cmyk.jpg'):\033[0m")
try:
    print(ft_load("landscape_cmyk.jpg"))
except Exception as e:
    print(f"\033[91mAssertionError: {e}\033[0m")
print()
