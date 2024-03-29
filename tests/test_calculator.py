import pytest

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


def test_different_delimiters():
    assert add('//;\n1;2') == 3
    
    
def test_not_allow_negatives():
    with pytest.raises(Exception) as e:
        add("-1")
    assert str(e.value) == "negatives not allowed -1"


def test_multiple_negatives():
    with pytest.raises(Exception) as e:
        add("-1,-2,4,-5")
    assert str(e.value) == "negatives not allowed -1, -2, -5"


def test_bigger_than_1000_should_be_ignored():
    assert add("2,1001") == 2


def test_1000_should_not_be_ignored():
    assert add("2,1000") == 1002


def test_long_delimiters():
    assert add("//[***]\n1***2***3") == 6
