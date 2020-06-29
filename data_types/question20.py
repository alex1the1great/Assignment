lists = ['abc', 'xyz', 'aba', '1221']
count = 0

for item in lists:
    if len(item) > 1:
        last_char = item[len(item) - 1]
        if item[0] == last_char:
            count += 1

print(count)