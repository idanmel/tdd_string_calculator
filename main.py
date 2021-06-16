
def normalize_numbers_from_string(s):
    result = s
    if s.startswith('//'):
        delimiter = s[2]
        s = s.replace('//' + delimiter + '\n', '')
        result = s.replace(delimiter, ',')

    return result


def replace_new_line_with_comma(s):
    new_string = s.replace('\n', ',')
    return new_string


def add(numbers):
    if numbers:
        numbers = normalize_numbers_from_string(numbers)
        numbers = replace_new_line_with_comma(numbers)
        numbers = numbers.split(",")
        return sum(int(x) for x in numbers)
    return 0
