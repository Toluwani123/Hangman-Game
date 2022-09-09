from words import word_bank
import random
import string

def get_word(words):
    word = random.choice(word_bank)
    while " " in word or "-" in word:
        word = random.choice(word_bank)
    return word.upper()

def hangman_game():
    word = get_word(word_bank)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guesses = set()
    lives = 10
    while len(word_letters) > 0:
        if lives < 10:
            print("You've used these letters: " , " ".join(guesses))
        list = [char if char in guesses else "-" for char in word]
        print("This is where you are now: ", " ".join(list))
        user_input = input("Enter a letter:").upper()

        if user_input in alphabet - guesses:
            guesses.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives = lives - 1
                print("You have {0} lives left".format(lives))

        elif user_input in guesses:
            print("You've used this word already")

        else:
            print("Letter doesn't exist")
    if lives > 0:
        print("You won congrats")
    else:
        print("You tried so hard to spell this word. {0}".format(word))

hangman_game()
    