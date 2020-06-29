given_char = 'A'
string = input('Enter a word: ')


check_char = lambda word: given_char in word[0]
print(check_char(string))
