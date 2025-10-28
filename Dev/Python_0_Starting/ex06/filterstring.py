import sys as system
import ft_filter as my

def main():
    """Output a list of words from the first argument (string) that have a length greater than the second argument (int)."""
    try:
        if len(system.argv) != 3:
            raise ValueError("the arguments are bad")
        try:
            size = int(system.argv[2])
        except ValueError:
            raise ValueError("the arguments are bad")
        
        word_list = [word for word in system.argv[1].split(" ") if word.isalnum()]
        print(my.ft_filter(lambda x: len(x) > size, word_list))
        exit(0)

    except Exception as e: 
        print(f"AssertionError: {e}")
        exit(1)


if __name__ == "__main__":
    main()