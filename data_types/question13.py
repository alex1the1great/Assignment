print('Example: red, blue, green, black')
comma_s_v = input('Enter comma separated values: ')

# split the input with comma
csv = comma_s_v.split(', ')
# sort the list
csv.sort()

unique_item = []

# iterate and check for unique_item
for item in csv:
    if item not in unique_item:
        unique_item.append(item)

# convet list into string
my_final = ', '.join(unique_item)
print(my_final)

