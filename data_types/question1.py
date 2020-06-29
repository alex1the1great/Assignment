string = input('Enter a string: ')
character_frequency = {}

for s in string:
    character_count = string.count(s)
    character_frequency[s] = character_count

print(character_frequency)
