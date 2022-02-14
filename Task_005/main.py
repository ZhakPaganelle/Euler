import functools


def get_primes(number: int) -> dict[int, int]:
    """Decomposes a number into prime factors"""
    primes = {}
    while number > 1:
        for i in range(2, number + 1):
            if number % i == 0:
                primes[i] = primes.get(i, 0) + 1
                number //= i
                break
    return primes


def smallest_multiple(biggest_number: int) -> int:
    """Returns smallest positive number that is evenly divisible by all of the numbers from 1 to n"""
    primes_dict = {}
    for number in range(1, biggest_number + 1):
        number_primes = get_primes(number)
        for prime in number_primes:
            primes_dict[prime] = max(number_primes[prime], primes_dict.get(prime, 0))
    return functools.reduce(
        lambda x, y: x * y,
        map(lambda x: x[0] ** x[1], primes_dict.items())
    )


if __name__ == '__main__':
    print(smallest_multiple(10))
    print(smallest_multiple(20))
