nth = int(input('Enter number between 1 to 15: '))


if nth >= 1 and nth <= 15:
    def square_dict(nth_item):
        sample_dict = {}

        for i in range(1, nth_item + 1):
            sample_dict[i] = i * i

        return sample_dict

    print(square_dict(nth))
else:
    print('Please enter with in range 1 - 15')



