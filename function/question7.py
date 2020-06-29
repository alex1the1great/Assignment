string = input('Enter a string: ')


def count_upper_lower(string):
    upper = 0
    lower = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            pass
    return f'Uppercase Characters: {upper} \nLowercase Characters: {lower}'


print(count_upper_lower(string))
