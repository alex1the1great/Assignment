import re

print('Example: 1 2 3 4 5')
numbers = input('Enter list of numbers separate with space:')

pattern = r'^[0-9\s]+$'
check_multi = re.findall(pattern, numbers)

if not check_multi:
    print('Please enter valid format')
else:
    initial = 0
    # convert numbers into list
    numbers_list = numbers.split(' ')
    for num in numbers_list:
        # typecasting str into int
        num = int(num)
        if initial < num:
            initial = num
    print('Largest number:', initial)
