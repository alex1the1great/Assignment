list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

new_list = list1[:len(list1)-1]

for i in list2:
    new_list.append(i)

print(new_list)