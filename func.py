import random
import time

def word_picker(word_list):
    picked_word = word_list[random.randint(0, len(word_list))]
    return picked_word


def initial_msg():
    print(("Hello, this is the game of Hangman Cutre Version. I'm gonna pick a word from SPANISH\n"
           "dictionary and you have to guess the word in less than 15 rounds. READY?"))
    time.sleep(3)  # 3s
    print("I'm thinking the word...")
    time.sleep(2.5)  # 2.5s
    print("Got it!! Now guess!")
    


def game_loop(word, word_sliced, bad_letters, good_letters):
    rounds = 15
    while rounds > 0:
        letter_guess = input("Which letter are you gonna choose?: ")
        letter_guess = letter_guess.lower()

        if letter_guess == word:
            print("YES! you win!")
            rounds = 0
        elif letter_guess not in word_sliced:
            print("No, try again!")
            bad_letters.append(letter_guess)
            print("The NOT CORRECT letters you choose are: {}".format(bad_letters))
            print("The correct letters you choose are: {}".format(good_letters))
            print("Round {}:".format(rounds - 1))
            rounds -= 1
        else:
            print("Yes, that is a correct letter!")
            good_letters.append(letter_guess)
            print("The NOT CORRECT letters you choose are: {}".format(bad_letters))
            print("The correct letters you choose are: {}".format(good_letters))
            print("Round {}:".format(rounds - 1))
            rounds -= 1

    print("The word was {}!".format(word))

