
def add(numbers):
    if numbers:
        numbers = numbers.split(",")
        return sum(int(x) for x in numbers)
    return 0


