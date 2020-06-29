string = 'Index'
new_string = ''

for char in enumerate(string):
    if char[0] % 2 == 0:
        new_string += char[1]

print(new_string)

