sample_list_dict = [
    {'name': 'Jane', 'age': 25},
    {'name': 'Max', 'age': 18},
    {'name': 'Hari', 'age': 40}
]

sort_list = sorted(sample_list_dict, key=lambda x: x['age'])

print(sort_list)