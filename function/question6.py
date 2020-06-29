number_present = int(input('Enter a number: '))


def check_number_present(number_present, numbers):
    if number_present in numbers:
        print('Number Found')
    else:
        print('Number Not Found')


check_number_present(number_present, [1, 2, 3, 4, 5])
