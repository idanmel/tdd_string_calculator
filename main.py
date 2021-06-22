
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


def get_numbers(numbers):
    return [int(x) for x in numbers]


def validate_numbers(numbers):
    negatives = [str(x) for x in numbers if x < 0]
    if negatives:
        raise ValueError("negatives not allowed %s" % ", ".join(negatives))


def add(numbers):
    if numbers:
        normalized_numbers = normalize_numbers_from_string(numbers)
        comma_numbers = replace_new_line_with_comma(normalized_numbers)
        split_numbers = comma_numbers.split(",")
        numbers = get_numbers(split_numbers)
        validate_numbers(numbers)
        return sum(numbers)
    return 0
