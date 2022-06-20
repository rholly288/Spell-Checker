#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Created By: Rachel Holly
# Created Date: 6/15/2022
# Last Edited: 6/18/2022
# Version: 1.01
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


print('Welcome to the Spell Checker Program! This program will find the incorrectly spelled words in a text file and '
      'make suggestions for corrections.')

keep_running = True
while keep_running:
    file_name = input('Please enter the file name: ')
    run_search(file_name)
    cont = input('Would you like to correct another file? (Y/N): ')
    if cont == 'N' or cont == 'n':
        keep_running = False

print('Thank you for using this Spell Check Program! Have a great day!')

