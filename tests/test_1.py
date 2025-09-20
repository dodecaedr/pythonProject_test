def add_numbers(a: int, b: int) -> int:
    return a + b


def is_even(a: int) -> int:
    return a % 2 == 0


def find_max(a: list) -> int:
    if len(a) > 0:
        return max(a)
    return 0


if __name__ == '__main__':
    assert add_numbers(2, 3) == 5

    assert is_even(2) == True

    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([]) == 0
