dic1 = {'name': 'Max', 'age': 15, 'address': 'UK'}

enter_key = input('Enter a key to remove: ')

if enter_key in dic1:
    del dic1[enter_key]
    print(dic1)
else:
    print('Invalid key name.')
