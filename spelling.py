#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Created By: Rachel Holly
# Created Date: 6/10/2022
# Last Edited: 6/18/2022
# Version: 1.06
# ----------------------------------------------------------------------------------------------------------------------
""" This module spell checks a given word by finding different spelling mistakes and cross-checking the corrected words
    with all the words in the English language. Its purpose is to be used with a class to correct misspelled words
     in a txt file."""
# ----------------------------------------------------------------------------------------------------------------------
# Import list of all the words in the English language
from nltk.corpus import words

word_list = words.words()


def real_word(words):
    """
    Finds words in a list that are valid words of the English language.
    :param words: a list of words
    :return: a set of words that exist in English
    """
    # Convert lists into sets to avoid duplicates
    unique_words = set(words)
    known_words = set(word_list)

    # Find the intersection of the two sets
    common = set(unique_words).intersection(known_words)
    return list(common)


def transposes(word):
    """
    Finds all the single transposes of adjacent letters in a word
    :param word: a string
    :return: a set of words with all the possible single transposes
    """
    # Establish an empty set to store words
    transposes = set()

    # Split word into a list of characters
    split = [char for char in word]

    # Go through list of characters.
    for i in range(len(split) - 1):
        # For every index, replace with the next index and make the next index the original
        split[i], split[i + 1] = split[i + 1], split[i]

        # Convert list back into string and append to list
        transposes.add(''.join(split))

        # Undo the transpose for the next index
        split[i + 1], split[i] = split[i], split[i + 1]
    return transposes


def letter_swap(word):
    """
    Replaces every letter in the word with each letter in the alphabet.
    Targets typos caused by typing the incorrect letter on the keyboard.
    :param word: a string
    :return: a set of words with every possible replacement of letters
    """
    # Establish an empty set to store words
    swaps = set()

    # Create a string of the alphabet
    letters = 'abcdefghijklmnopqrstuvwxyz'

    # Replace every letter in the word with every letter of the alphabet and add to set
    for char in word:
        for l in letters:
            new = word.replace(char, l)
            swaps.add(new)
    return swaps


def add_letter(word):
    """
    Individually adds every letter in the alphabet next to each letter in the word provided.
    Aims to correct the spelling mistake of missing a letter in the word.
    :param word: a string
    :return: a set of all the words with added letters
    """
    # Establish an empty set to store words
    added = set()

    # Create a string of the alphabet
    letters = 'abcdefghijklmnopqrstuvwxyz'

    # Individually add every letter in the alphabet next to every letter in the word and add new word to the set.
    for char in word:
        for l in letters:
            new = word.replace(char, char + l)
            added.add(new)
    return added


def del_letter(word):
    """
    Individually deletes every letter in the word provided.
    Aims to correct the spelling mistake of hitting two keys at once and having an extra letter in the word.
    :param word: a string
    :return: a set of all the new words with deletions
    """
    # Establish an empty set to store words
    deleted = set()

    # Individually delete every letter in the word and add new word to the set.
    for char in word:
        new = word.replace(char, '')
        if new not in deleted:
            deleted.add(new)
    return deleted


def duplicate_letters(word):
    """
    Replaces single letters with double letters, double letters with single letters, and triple letters with double
    letters. Aims to solve the issue of repeating letters adjacently and incorrect number of times.
    :param word: a string
    :return: a set of all the words with all possible letter repetitions
    """
    # Establish an empty set to store words
    dups = set()

    # Individually replace every letter in the word with the same letter twice and add new word to set.
    for char in word:
        new = word.replace(char, char * 2)
        dups.add(new)

    # Individually replace every letter appearing 3 times consecutively with the letter twice and add new word to set.
    for char in word:
        if char * 3 in word:
            new = word.replace(char * 3, char * 2)
            dups.add(new)

    # Individually replace every double letter in the word with the letter once and add the new word to the set.
    for char in word:
        if char * 2 in word:
            new = word.replace(char * 2, char)
            dups.add(new)
    return dups


def capitalization(word):
    """
    Searches for proper nouns by capitalizing the first letter of the word
    :param word: a string
    :return: the capitalized word in a set
    """
    # Create an empty set to store the word
    cap = set()

    # Split word into a list of characters
    split = [char for char in word]

    # Find the order of the first character and change it to its capitalized order.
    num = ord(split[0])
    capital = num - 32
    letter_new = chr(capital)

    # Replace the first letter with the capitalized one and add the word to the set.
    split[0] = letter_new
    new = ''.join(split)
    cap.add(new)
    return cap


def all_mistakes(word):
    """
    Find all the mistakes in a word by checking each spelling mistake.
    :param word: a string
    :return: a set of all the possible words that the word could be
    """
    # Create set of all errors by finding the union of all the sets of corrections
    all_errors = transposes(word) | letter_swap(word) | add_letter(word) | del_letter(word) | duplicate_letters(word) \
                 | capitalization(word)
    return all_errors


def multiple_mistakes(word):
    """
    Checks for multiple mistakes in a single word.
    :param word: a string
    :return: a list of all the possible words containing two mistakes
    """
    # Passes word through the all_mistakes function and then every word in the result through the function again.
    lst = [total for sub_total in all_mistakes(word) for total in all_mistakes(sub_total)]
    return real_word(lst)

