import re

print('Example: 1 2 3 4 5')
numbers = input('Enter list of numbers separate with space:')

pattern = r'^[0-9\s]+$'
check_multi = re.findall(pattern, numbers)

if not check_multi:
    print('Please enter valid format')
else:
    total = numbers.split(' ')
    product = 1
    for i in total:
        i = int(i)
        product *= i
    print(product)
