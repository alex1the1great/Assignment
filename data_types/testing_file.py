import re

string = input('Enter a string: ')

pattern = '^[a-zA-Z]+$'
check_it = re.findall(pattern, string)

print(check_it)