#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Created By: Rachel Holly
# Created Date: 6/15/2022
# Last Edited: 6/18/2022
# Version: 1.03
# ----------------------------------------------------------------------------------------------------------------------
""" This is the main.py module for the Spell Checker. This module prompts user input for a file name and works alongside
the searching class and spelling module to return the misspelled words in the text file and the list of possible
correctly spelled words for the user to browse."""
# ----------------------------------------------------------------------------------------------------------------------
# Import searching class
from searching import Searching


def run_search(file_name):
    """
    Takes a file name and runs through the class Searching
    :param file_name: name of the file
    :return: prints results
    """
    file = Searching(file_name)
    # Call functions within the class
    file.open_file()
    file.search_file()
    file.get_corrections()
    return print(file.__str__())


def no_corrections(file_name):
    """
    Checks if there are any corrections misspelled words.
    :param file_name: name of the file
    :return: True if there are no misspelled words. False otherwise
    """
    file = Searching(file_name)
    file.open_file()
    # If file.search_file returns an empty list, then there are no misspelled words
    if not file.search_file():
        return True
    else:
        return False


def edits(file_name, incorrect, correction):
    """
    Replaces misspelled words in the file with correctly spelled words
    :param file_name: name of the file
    :param incorrect: incorrectly spelled word
    :param correction: correctly spelled word
    :return: edited file
    """
    file = Searching(file_name)
    file.edit_file(incorrect, correction)


print('Welcome to the Spell Checker Program! This program will find the incorrectly spelled words in a text file and '
      'make suggestions for corrections.')

# Set variable to establish a loop if user has multiple files to check
keep_running = True
while keep_running:
    # Ask for file name and use the run_search function to call the spelling class
    file_name = input('Please enter the file name: ')
    run_search(file_name)

    # If there are no misspelled words, ask for another file but do not ask to make edits to current file
    if no_corrections(file_name):
        cont = input('Would you like to correct another file? (Y/N): ')
    else:
        # Ask user if they would like to replace words in their text file
        edit = input('Would you like to replace any of the above misspelled words in the text file? (Y/N): ')

        # Establish loop for multiple edits
        multiple_edits = True
        while multiple_edits:
            if edit == 'Y' or edit == 'y':
                # Get incorrectly and correctly spelled word
                incorrect = input('Which misspelled word would you like to replace: ')
                correction = input('Which word would you like to replace it with: ')

                # Call edits function to edit the file in the class
                edits(file_name, incorrect, correction)
                print('The correction has been made to the file.')

                # Ask if another edit should be made
                edit = input('Is there another word you\'d like to replace? (Y/N): ')
            if edit == 'N' or edit == 'n':
                multiple_edits = False

        # Check if there is another file to correct.
        cont = input('Would you like to correct another file? (Y/N): ')

    # If there are no more files, break out of loop and display goodbye message.
    if cont == 'N' or cont == 'n':
        keep_running = False

print('Thank you for using this Spell Check Program! Have a great day!')

