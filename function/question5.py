positive_num = int(input('Enter positive number: '))


def factorial(positive_num):
    # if positive
    if positive_num > 0:
        fact = 1
        for i in range(1, positive_num+1):
            fact *= i
        return fact
    # num = 0
    elif positive_num == 0:
        return 0
    else:
        return 'Please enter positive number only.'


print(factorial(positive_num))
