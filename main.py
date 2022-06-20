#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Created By: Rachel Holly
# Created Date: 6/15/2022
# Last Edited: 6/18/2022
# Version: 1.02
# ----------------------------------------------------------------------------------------------------------------------
""" This is the main.py module for the Spell Checker. This module prompts user input for a file name and works alongside
the searching class and spelling module to return the misspelled words in the text file and the list of possible
correctly spelled words for the user to browse."""
# ----------------------------------------------------------------------------------------------------------------------
from searching import Searching


def run_search(file_name):
    file = Searching(file_name)

    file.open_file()
    file.search_file()
    file.get_corrections()
    print(file.__str__())


def edits(filename, incorrect, correction):
    file = Searching(file_name)
    file.edit_file(incorrect, correction)


print('Welcome to the Spell Checker Program! This program will find the incorrectly spelled words in a text file and '
      'make suggestions for corrections.')

keep_running = True
while keep_running:
    file_name = input('Please enter the file name: ')
    run_search(file_name)
    edit = input('Would you like to replace any of the above misspelled words in the text file? (Y/N): ')
    multiple_edits = True
    while multiple_edits:
        if edit == 'Y' or edit == 'y':
            incorrect = input('Which misspelled word would you like to replace: ')
            correction = input('Which word would you like to replace it with: ')
            edits(file_name, incorrect, correction)
            print('The correction has been made to the file.')
        edit = input('Is there another word you\'d like to replace? (Y/N): ')
        if edit == 'N' or edit == 'n':
            multiple_edits = False

    cont = input('Would you like to correct another file? (Y/N): ')
    if cont == 'N' or cont == 'n':
        keep_running = False

print('Thank you for using this Spell Check Program! Have a great day!')

