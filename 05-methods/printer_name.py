"""Simple demonstration of the "if __name__ == "__main__" guard"""

# Read more at https://realpython.com/if-name-main-python/


def print_text(text: str = "Some default text"):
    print(f"{text}\n" * 5)


# Here we check to see if the file is being called directly. If it is,
# we run the function call:
if __name__ == "__main__":
    print_text("Hello")
