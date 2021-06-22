
def get_multichar_delimiter(s):
    last_par_index = s.index(']')
    return ''.join(s[3:last_par_index])


def drop_delimiter_frame(s, delimiter, multi=False):
    if multi:
        return s.replace('//[' + delimiter + ']\n', '')
    return s.replace('//' + delimiter + '\n', '')


def normalize_numbers_from_string(s):
    result = s
    if s.startswith('//'):
        try:
            delimiter = get_multichar_delimiter(s)
            s = drop_delimiter_frame(s, delimiter, multi=True)
        except ValueError:
            delimiter = s[2]
            s = drop_delimiter_frame(s, delimiter)
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
        valid_numbers = [number for number in numbers if number <= 1000]
        return sum(valid_numbers)
    return 0


# sum -> reduce [...] fn(1,2), fn(2,3)
# sum -> reduce + [1,2,3,4,5], [3,3,4,5], [6,4,5] [10,5] 15
# map -> [1,2,3,4,5] [1,4,9,16,25] [3,6,9,12,15] [number * 3 for number in numbers]
# filter -> [1,2,3,4,5] x < 4 [number for number in numbers if number < 4] == [1,2,3]

