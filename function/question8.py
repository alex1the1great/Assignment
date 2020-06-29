def check_append(numbers):
    new_list = []

    for i in numbers:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(check_append([1, 2, 3, 3, 2, 4, 5, 5]))
