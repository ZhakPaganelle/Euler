def is_prime(number: int) -> bool:
    """Returns if number is prime"""
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5 + 1), 2):
        if number % i == 0:
            return False
    return True


def get_biggest_prime_divider(number: int) -> int:
    """Returns biggest prime divider of the number"""
    for i in range(number // 2 + (1 - number % 2), 1, -2):
        if number % i == 0 and is_prime(i):
            return i
    return 0


if __name__ == '__main__':
    print(get_biggest_prime_divider(13195))
    print(get_biggest_prime_divider(600851475143))
