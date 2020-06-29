number_list = [1, 2, 3, 4]

string = input('Enter a string: ')

new_list = map(lambda x: string + str(x), number_list)

print(list(new_list))