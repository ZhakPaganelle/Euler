import functools
from typing import List


def fibonacci_less_than(number: int) -> List[int]:
    """Returns list of Fibonacci numbers which are less than given number"""
    fibonacci = [1, 2]
    while fibonacci[-1] < number:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:-1]


def get_even_fibonacci_sum_less_than(number: int) -> int:
    """Returns sum of even Fibonacci numbers which are less than given number"""
    return functools.reduce(
        lambda x, y: x + y,
        (i for i in fibonacci_less_than(number) if i % 2 == 0)
    )


if __name__ == '__main__':
    print(fibonacci_less_than(100))
    print(get_even_fibonacci_sum_less_than(4_000_000))
