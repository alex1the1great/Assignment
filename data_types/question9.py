string = input('Enter a string: ').lower()
# nth character + [1:n-1] + first character
new_string = string[len(string)-1] + string[1:len(string)-1] + string[0]

print(new_string.title())

