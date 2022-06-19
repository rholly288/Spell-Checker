#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Created By: Rachel Holly
# Created Date: 6/17/2022
# Last Edited: 6/18/2022
# Version: 1.00
# ----------------------------------------------------------------------------------------------------------------------
""" This function creates a set of all the words in the English language by merging two data sets. One, sourced from
nltk, contains proper nouns but does not contain common suffix's like -ed, -ing, or -s. The second data set contain
these common endings. Together, these sets will provide a thorough set of all the words in the English language for the
misspelled words to be compared to."""
# ----------------------------------------------------------------------------------------------------------------------
# Import list of all the words in the English language
from nltk.corpus import words


def known_words(file_name):
    with open(file_name, 'r') as f:
        dict = [word.rstrip() for word in f]
        words_1 = set(dict)
    words_2 = set(words.words())
    known = words_1 | words_2
    return known
