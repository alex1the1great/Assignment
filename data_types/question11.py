sentence = 'This is just an example and this example are not good'.lower()
word_frequency = {}

# split sentence with space and return list of each word.
new_sentence = sentence.split(' ')

for word in new_sentence:
    # count word occurrence in new_sentence list.
    word_count = new_sentence.count(word)
    # set word with word count into dictionary.
    word_frequency[word] = word_count

print(word_frequency)
