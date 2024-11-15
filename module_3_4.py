def single_root_words(root_word='', *other_words):
    root_word = root_word.upper()
    same_words = []

    for i in other_words:
        s = i.upper()
        if root_word in s:
            same_words.append(i)
        if s in root_word:
            same_words.append(i)
    return same_words


single_root_words()

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
