def single_root_words(root_word, *other_words):
    some_words = []
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            some_words.append(other_words[i])
    return some_words


print(single_root_words('DiSable', 'Able', 'kassa', 'mass', 'dfer'))
print(single_root_words('Fe', 'Able', 'kassa', 'mass', 'dfEr'))
print(single_root_words('AS', 'Able', 'kAssa', 'Mass', 'dfer'))