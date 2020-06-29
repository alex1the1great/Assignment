string = input('Enter a string: ')
string_length = len(string)
first_last_string = ''

if string_length < 2:
    print('Empty String')
elif string_length == 2:
    print(f'{string * 2}')
elif string_length == 3:
    print(f'{string[0]}{string[1] * 2}{string[2]}')
else:
    print(f'{string[0]}{string[1]}{string[string_length-2]}{string[string_length-1]}')

