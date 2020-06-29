lists = [1, 2, 3, 2, 4, 3]
new_list = []

for i in lists:
    if i not in new_list:
        new_list.append(i)


print(new_list)