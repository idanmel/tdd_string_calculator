
def replace_new_line_with_comma(s):
    new_string = s.replace('\n', ',')
    return new_string


def add(numbers):
    if numbers:
        numbers = replace_new_line_with_comma(numbers)
        numbers = numbers.split(",")
        return sum(int(x) for x in numbers)
    return 0
