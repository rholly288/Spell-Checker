from nltk.corpus import words
word_list = words.words()


def real_word(words):
    unique_words = set(words)
    known_words = set(word_list)
    common = set(unique_words).intersection(known_words)
    return list(common)


def transposes(word):
    transposes = []
    split = [char for char in word]
    for i in range(len(split) - 1):
        split[i], split[i + 1] = split[i + 1], split[i]
        transposes.append(''.join(split))
        split[i + 1], split[i] = split[i], split[i + 1]
    return transposes


def letter_swap(word):
    swaps = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for char in word:
        for l in letters:
            new = word.replace(char, l)
            if new not in swaps:
                swaps.append(new)
    return swaps


def add_letter(word):
    add = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for char in word:
        for l in letters:
            new = word.replace(char, char + l)
            if new not in add:
                add.append(new)
    return add


def del_letter(word):
    deleted = []
    for char in word:
        new = word.replace(char, '')
        if new not in deleted:
            deleted.append(new)
    return deleted


def duplicate_letters(word):
    dups = []
    for char in word:
        new = word.replace(char, char * 2)
        if new not in dups:
            dups.append(new)
    for char in word:
        if char * 3 in word:
            new = word.replace(char * 3, char * 2)
            if new not in dups:
                dups.append(new)
    for char in word:
        if char * 2 in word:
            new = word.replace(char * 2, char)
            if new not in dups:
                dups.append(new)
    return dups


def all_mistakes(word):
    all_errors = set(transposes(word) + letter_swap(word) + add_letter(word) + del_letter(word) + duplicate_letters(word))
    return all_errors


def multiple_mistakes(word):
    lst = [total for sub_total in all_mistakes(word) for total in all_mistakes(sub_total)]
    print(lst)
    return real_word(lst)



