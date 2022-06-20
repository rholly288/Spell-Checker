# Spell-Checker
Final Project for EECE2140

This program takes a text file provided by the user and searches for misspelled words. The misspelled words are then manipulated using common spelling mistakes to create a list of possible corrections. These corrections are displayed to the user with a "Did you mean ...?" prompt followed by the list of corrections. After all the words and their corrections are printed, the user has the choice to edit their text file by providing the misspelled word they'd like to replace and the correct word they want to replace it with. After the file has been edited, the user has the option of spell-checking another file. When the user is finished, a goodbye message will appear.

Uploaded files:

dictionary.txt - This text file contains a list of words in the English Language provided by Dr. Phillip M. Feldman. This list contains words with common suffix's like  -s, -ing, and -ed that the nltk library did not. More details about this file can be viewed using the website: https://phillipmfeldman.org/English/spelling%20dictionaries.html

dictionary.py - This module contains a single function that creates a set of the words in the dictionary.txt file along with the list of words provided by the nltk library. The nltk library list contains proper nouns that the dictionary.txt file does not. These are used in junction for a more thorough for misspelled words. It is imported in both the spelling module and searching class.

spelling.py - This module spell checks a given word by finding different spelling mistakes and cross-checking the corrected words with all the words in the English language. Its purpose is to be used with the searching class to correct misspelled words in a txt file.

searching.py - This class takes a filename and sorts through the file to find all the misspelled words in the file. It then will print the resulting list of possible words in a string with the sentence the word came from.

main.py - This module prompts user input for a file name and works alongside the searching class and spelling module to return the misspelled words in the text file and the list of possible correctly spelled words for the user to browse. This module contains all of the user input for the program. Three functions are defined in this module to call the searching class in order to find misspelled words, their corrections, and edit the text file.

Other useful information:
The nltk library is used in this program for their list of English words and their function that splits a block of text into a list of sentences. In pycharm, the library can be added by going to File > Settings > Project. Select your current project. Then click Python Interpreter, the + symbol, and search nltk. Click install package.
Information on how to install the library can be found on their website: https://www.nltk.org/install.html
