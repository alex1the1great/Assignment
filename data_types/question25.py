sample_list = [{}, {}, {1, 2}]

for dics in sample_list:
    if len(dics) != 0:
        print('Non Empty Dictionary')
        break
else:
    print('Empty Dictionary')
