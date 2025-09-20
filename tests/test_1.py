from src.main import find_max, is_even, add_numbers, divide


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_is_even():
    assert is_even(2) == True


def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5

    assert find_max([]) == 0


def test_divide():
    assert divide(2, 1) == 2

    assert divide(2, 2) == 1
