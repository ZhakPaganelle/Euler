import functools


def get_sum_div_3_5(number: int) -> int:
    """Returns sum of multiples of 3 or 5 until given number"""
    return functools.reduce(lambda x, y: x + y, (i for i in range(number) if i % 3 == 0 or i % 5 == 0))


if __name__ == '__main__':
    print(get_sum_div_3_5(10))
    print(get_sum_div_3_5(1000))
