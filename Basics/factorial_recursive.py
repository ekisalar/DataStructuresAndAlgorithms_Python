# Define two functions that find the factorial of two number.
# One should use recursive, the other should use a for loop


def find_factorial_recursive(number):
    if number == 2:
        return 2
    return number * find_factorial_recursive(number - 1)


def find_factorial_iterative(number) -> int:
    result = number
    for i in range(number - 1, 1, -1):
        result = result * i
    return result

# from factorial_recursive import find_factorial_iterative, find_factorial_recursive
#
# result = find_factorial_iterative(5)
# print(result)
#
# result1 = find_factorial_recursive(5)
# print(result1)
