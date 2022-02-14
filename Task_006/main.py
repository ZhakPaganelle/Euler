import functools


def square_sum(last_number: int) -> int:
    """Returns square of the sum of the numbers from 1 to n"""
    return sum(range(last_number + 1)) ** 2


def sum_of_squares(last_number: int) -> int:
    """Returns sum of squares of the numbers from 1 to n"""
    return sum([i ** 2 for i in range(last_number + 1)])


if __name__ == '__main__':
    print(square_sum(10) - sum_of_squares(10))
    print(square_sum(100) - sum_of_squares(100))
