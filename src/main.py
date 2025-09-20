def add_numbers(a: int, b: int) -> int:
    return a + b


def is_even(a: int) -> int:
    return a % 2 == 0


def find_max(a: list) -> int:
    if len(a) > 0:
        return max(a)
    return 0


def x(a: list, b: list):
    list_1 = []
    for i in a:
        if i in b:
            list_1.append(i)
    return list_1


def divide(a, b):
    if b > 0:
        return a / b
    return 0
