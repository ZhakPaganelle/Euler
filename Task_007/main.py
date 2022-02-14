from typing import Iterator


def is_prime(number: int) -> bool:
    """Returns if number is prime"""
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5 + 1), 2):
        if number % i == 0:
            return False
    return True


def prime_iter() -> Iterator:
    """Yields primes"""
    number = 1
    while True:
        if is_prime(number):
            yield number
        number += 1


def prime_number_n(n: int) -> int:
    """Returns nth prime number"""
    for i, prime in enumerate(prime_iter()):
        if i == n - 1:
            return prime


if __name__ == '__main__':
    print(prime_number_n(6))
    print(prime_number_n(10001))
