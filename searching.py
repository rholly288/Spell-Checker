#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Created By: Rachel Holly
# Created Date: 6/13/2022
# Last Edited: 6/18/2022
# Version: 1.02
# ----------------------------------------------------------------------------------------------------------------------
""" This class takes a filename and sorts through the file to find all the misspelled words in the file. It then will
print the resulting list of possible words in a string with the sentence the word came from."""
# ----------------------------------------------------------------------------------------------------------------------
import string
import nltk
import spelling
import dictionary


class Searching:
    known_words = dictionary.known_words('dictionary.txt')

    def __init__(self, file_name):
        self.file = file_name
        self.words = []
        self.misspelled_words = []
        self.sentences = []
        self.corrections = {}

    def open_file(self):
        no_punctuation = ''
        with open(self.file, encoding='utf8') as f:
            text = f.read()
            for word in text:
                if word not in string.punctuation:
                    no_punctuation += word
            self.words = no_punctuation.split()
            self.sentences = nltk.tokenize.sent_tokenize(text)

    def search_file(self):
        for word in self.words:
            if word not in Searching.known_words:
                split = [char for char in word]
                num = ord(split[0])
                capital = num + 32
                letter_new = chr(capital)
                split[0] = letter_new
                new = ''.join(split)
                if new not in Searching.known_words:
                    self.misspelled_words.append(word)

    def get_corrections(self):
        for word in self.misspelled_words:
            self.corrections[word] = spelling.multiple_mistakes(word)

    def __str__(self):
        result = ''
        for word in self.misspelled_words:
            for sentence in range(len(self.sentences)):
                if word in self.sentences[sentence]:
                    result += f'For "{word}" in the following sentence: \n{self.sentences[sentence]}\n'
                    result += 'Did you mean any of the following words: \n'
                    result += ', '.join(self.corrections[word])
                    result += '\n'
            result += '\n'
        return result
