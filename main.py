import random
import time

WORDLIST = ["cuerpo", "pierna", "pie", "talon", "espinilla", "rodilla", "muslo", "cabeza", "cara", "boca", "labio",
            "diente", "ojo", "nariz", "barba", "bigote", "cabello", "oreja", "cerebro", "estomago", "brazo", "codo",
            "hombro", "uña", "mano", "muñeca", "palma", "dedo", "trasero", "culo", "cola", "gluteos", "abdomen",
            "higado", "musculo", "cuello", "corazon", "mente", "alma", "espiritu", "pecho", "cintura", "cadera",
            "espalda", "sangre", "carne", "piel", "hueso", "resfriado", "gripe", "diarrea", "salud", "enfermedad"]


def word_picker(word_list):
    picked_word = word_list[random.randint(0, len(word_list))]
    return picked_word


def initial_msg():
    print(("Hello, this is the game of Hangman Cutre Version. I'm gonna pick a word from the human\n"
           "body or health, in SPANISH, and you have to guess the word in less than 10 rounds. READY?"))
    time.sleep(5)  # 5s
    print("I'm thinking the word...")
    time.sleep(2.5)  # 2.5s
    print("Got it!! Now guess!")


def game():
    rounds = 10
    initial_msg()
    word = word_picker(WORDLIST)
    print("The word has {} letters.".format(len(word)))
    print()
    word_sliced = list(word)  # separates each letter of the word and places into a list
    good_letters = []
    bad_letters = []

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


game()
