from main import add


def test_empty_string_should_return_zero():
    assert add("") == 0


def test_single_char_string_should_return_number():
    number = "1"
    assert add(number) == 1


def test_two_numbers_should_return_sum():
    numbers = "1,2"
    assert add(numbers) == 3


def test_multiple_numbers_should_return_sum():
    numbers = "1,2,3,4,5"
    assert add(numbers) == 15


def test_newline_delimiter_works():
    assert add('1\n2,3') == 6
