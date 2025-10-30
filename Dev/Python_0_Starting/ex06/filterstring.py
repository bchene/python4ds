import sys as system
import ft_filter as my


def main():
    """Output a list of words from the first argument (string) that have a
     length greater than the second argument (int)."""
    try:
        assert len(system.argv) == 3, "2 arguments are required"
        assert system.argv[2].isdigit(), "second argument must be an integer"

        word_list = [
            word for word in system.argv[1].split(" ") if word.isalnum()
        ]
        print(my.ft_filter(lambda x: len(x) > int(system.argv[2]), word_list))
        exit(0)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except Exception as e:
        print(f"Exception: {e}")
        exit(1)


if __name__ == "__main__":
    main()
