tuples = (1, 2, 3, 4, 5, 6, 7)


def tuple_length(tuples):
    counter = 0
    for i in tuples:
        counter += 1

    return counter


print(tuple_length(tuples))