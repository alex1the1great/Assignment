import re

string = input('Enter a string: ')

# Regex to check include string only or not
pattern = pattern = r'^[a-zA-Z\s]+$'
check_str = re.findall(pattern, string)

# If pattern not match
if not check_str:
    print('Please enter valid string.')
else:
    # convert to upper and lower cases
    lower_string = string.lower()
    upper_string = string.upper()

    print('Original:', string)
    print('Lower:', lower_string)
    print('Upper:', upper_string)
