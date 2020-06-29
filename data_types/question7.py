def word_length(words):
    initial_word_length = 0
    hold_index = 0

    for word in enumerate(words):
        check_len = len(word[1])

        if initial_word_length < check_len:
            initial_word_length = check_len
            hold_index = word[0]

    return words[hold_index]


longest_word = word_length(['Remembering', 'Tom', 'Cool', 'Elephant'])
print(f'{longest_word}: {len(longest_word)}')
