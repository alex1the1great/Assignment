nth = int(input('Enter a range: '))
sample_dict = {}

for i in range(1, nth + 1):
    values = i * i
    sample_dict[i] = values


print(sample_dict)