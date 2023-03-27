"""Prints 5 copies of given text on a line"""


def print_text(text: str = "No text provided"):
    print(f"{text}\n" * 5)


print_text("Printing text…")
