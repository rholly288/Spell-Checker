#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Created By: Rachel Holly
# Created Date: 6/13/2022
# Last Edited: 6/21/2022
# Version: 1.04
# ----------------------------------------------------------------------------------------------------------------------
""" This class takes a filename and sorts through the file to find all the misspelled words in the file. It then will
print the resulting list of possible words in a string with the sentence the word came from."""
# ----------------------------------------------------------------------------------------------------------------------
import string
import nltk
import spelling
import dictionary


class Searching:
    """ This class can open a file, search for misspelled words in the file, find corrections, edit the file, and
    return a string of the misspelled words and their corrections."""

    # Establish list of known_words from dictionary.py
    known_words = dictionary.known_words('dictionary.txt')

    def __init__(self, file_name):
        """
        Establishes variables for the file.
        :param file_name: the name of the file
        """
        self.file = file_name
        self.words = []
        self.misspelled_words = []
        self.sentences = []
        self.corrections = {}

    def open_file(self):
        """
        Opens the file and strips the text into a list of all the words and a list of all the sentences.
        :return: List of words and sentences from the file
        """
        no_punctuation = ''
        with open(self.file, encoding='utf8') as f:
            text = f.read()
            for word in text:
                # Strip punctuation before adding word to the list.
                # Contractions exist in known_word set without their apostrophe.
                if word not in string.punctuation:
                    no_punctuation += word
            # Add words and sentences to their respective lists.
            self.words = no_punctuation.split()
            self.sentences = nltk.tokenize.sent_tokenize(text)
        return self.words, self.sentences

    def search_file(self):
        """
        Searches through the file for misspelled words
        :return: A list of misspelled words
        """
        for word in self.words:
            if word not in Searching.known_words:
                # Check if a word exists in known_words when the first letter is not capitalized.
                # Corrects the mistake of adding the first word in a sentence to the misspelled list
                split = [char for char in word]
                num = ord(split[0])
                capital = num + 32
                letter_new = chr(capital)
                split[0] = letter_new
                new = ''.join(split)
                # If word is still not in the known_words set, then it is misspelled
                if new not in Searching.known_words:
                    self.misspelled_words.append(word)
        return self.misspelled_words

    def get_corrections(self):
        """
        Gets corrections for each misspelled word from the spelling module
        :return: A dictionary of the corrections for each word.
        """
        for word in self.misspelled_words:
            self.corrections[word] = spelling.multiple_mistakes(word)
        return self.corrections

    def edit_file(self, incorrect, correction):
        """
        Edits the text file by replacing a word with another
        :param incorrect: an incorrectly spelled word
        :param correction: a correctly spelled word
        :return: an edited text file
        """
        # Open text file to search for incorrectly spelled word.
        with open(self.file, 'r', encoding='utf8') as f:
            text = f.read()
            text = text.replace(incorrect, correction)
        # Open text file to write correctly spelled word into the file
        with open(self.file, 'w', encoding='utf8') as f:
            f.write(text)

    def __str__(self):
        """
        Formats the misspelled words, the sentence they appear in, and their corrections
        :return: a string
        """
        # If there are no misspelled words, return a confirmation message
        if not self.misspelled_words:
            return 'There are no spelling mistakes in the text provided.'
        else:
            # For each word, print its sentence and list of possible corrections
            result = ''
            for word in self.misspelled_words:
                for sentence in range(len(self.sentences)):
                    if word in self.sentences[sentence]:
                        result += f'\nFor "{word}" in the following sentence: \n{self.sentences[sentence]}\n'
                        result += 'Did you mean any of the following words: \n'
                        result += ', '.join(self.corrections[word])
                        result += '\n'
            return result
