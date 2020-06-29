sentence = input('Enter a sentence: ')

check_not = sentence.find('not')
check_poor = sentence.find('poor')

if (check_not and check_poor) == -1:
    print('Same ->', sentence)
else:
    if check_not < check_poor:
        replacer_sentence = sentence[check_not:check_poor+5]
        new_sentence = sentence.replace(replacer_sentence, 'good')
        print(new_sentence)
    else:
        print('Same ->', sentence)
