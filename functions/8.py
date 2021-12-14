
# Wrap the operations into one function, now named `calculate`,
# with a mandatory "operation" parameter.

def calculate(x: int, y: int, operation: str) -> int:
    """Calculates the sum (or difference) of two numbers.

    Parameters:
    `x` : int
        The first number
    `y` : int, optional
        The second number (default is 1)
    `operation`: str, optional
        The operation to perform (default is addition)
    """

    if operation == "subtract":
        return x - y
    else:
        return x + y


# Get two inputs from the user and cast them to integers
print("Enter a number:")
first = int(input())

print("Enter another number:")
second = int(input())

# Print the results of the two calculations
result = calculate(first, second)
print(f"The sum of {first} and {second} is {result}.")

result = calculate(first, second, operation="subtract")
print(f"{first} minus {second} is {result}.")
