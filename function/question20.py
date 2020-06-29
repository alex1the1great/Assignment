list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 8, 7]

result = filter(lambda x: x in list1, list2)
print(list(result))