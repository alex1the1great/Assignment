numbers = [10, 2, -3, 4, 3]


def multiple(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


print(multiple(numbers))
