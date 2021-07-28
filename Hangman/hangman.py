import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly choose a word
    # We don't want a word with a - or a space in it
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # unique letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: # in alphabet but not in used_letters
            used_letters.add(user_letter) # add to used_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter) # remove the guessed letter from the set of letters making up our word
            else:
                lives = lives - 1 # take away 1 life for being wrong
                print('Guessed letter is not in the word.')
        elif user_letter in user_letter:
            print('You have already used that character, please try again.')
        else:
            print('Invalid character, please try again.')

    # gets here when len(word_letters) == 0 or lives == 0
    if lives == 0:
        print('You died')
        print('The correct word was', word)
    else:
        print('You guessed the word correctly!')
hangman()
