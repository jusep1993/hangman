import random
import time
from func import *
from words_list import WORDLIST


def game():
    initial_msg()
    word = word_picker(WORDLIST)
    print("The word has {} letters.".format(len(word)))
    print()
    word_sliced = list(word)  # separates each letter of the word and places into a list
    good_letters = []
    bad_letters = []

    game_loop(word, word_sliced, bad_letters, good_letters)
  
game()
