import re

string = input('Enter a word: ')
string_length = len(string)

# Regex to check include string only or not
pattern = pattern = '^[a-zA-Z]+$'
check_str = re.findall(pattern, string)

if not check_str:
    print('Please only a word.')
else:
    if string_length < 3:
        print(string)
    else:
        check_ing = string[string_length - 3:]
        if check_ing == 'ing':
            new_string = string + 'ly'
            print(new_string)
        else:
            new_string = string + 'ing'
            print(new_string)


