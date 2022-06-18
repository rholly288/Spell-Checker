from nltk.corpus import words
word_list = words.words()


def real_word(words):
    possible_matches = []
    for word in words:
        if word in word_list:
            possible_matches.append(word)
    return possible_matches


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


def multiple_mistakes(word):
    mm = []
    first = transposes(word)
    for word in first:
        words = letter_swap(word)
        mm.extend(words)
    return real_word(mm)


print(multiple_mistakes('vefalut'))