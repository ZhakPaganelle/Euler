def is_palindrome(number: int) -> bool:
    """Returns if number is palindrome"""
    str_number = str(number)
    return str_number == str_number[::-1]


def get_biggest_palindrome_product(digits: int) -> int:
    """Returns the largest palindrome made from the product of two n-digit numbers"""
    palindromes = []
    for x in range(10 ** digits, 10 ** (digits - 1), -1):
        for y in range(10 ** digits, 10 ** (digits - 1), -1):
            if is_palindrome(x * y):
                palindromes.append(x * y)
    return max(palindromes)


if __name__ == '__main__':
    print(get_biggest_palindrome_product(2))
    print(get_biggest_palindrome_product(3))
