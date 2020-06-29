num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
num3 = int(input('Enter num3: '))


def max_finder(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print('Largest:', num1)
    elif num2 > num1 and num2 > num3:
        print('Largest:', num2)
    else:
        print('Largest:', num3)


max_finder(num1, num2, num3)
