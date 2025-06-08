def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) or not isinstance(y, (int, float))):
        return -1

    # Swapping without using a third variable
    x, y = y, x
    result= print("x:", x, "y:", y)

# Task 2
# Test the function with given inputs
result1 = swap("Apple", 10)
print("Result 1:", result1)

result2 = swap(9, 17)
print("Result 2:", result2)
