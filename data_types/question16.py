import re

print('Example: 1 2 3 4 5')
numbers = input('Enter list of numbers separate with space:')

pattern = r'^[0-9\s]+$'
check_nums = re.findall(pattern, numbers)

if not check_nums:
    print('Please enter valid format')
else:
    # convert numbers into list
    total = numbers.split(' ')
    sum_num = 0
    for i in total:
        # typecasting str to int
        i = int(i)
        sum_num += i
    print(sum_num)

