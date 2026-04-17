import random
import string

from words import words_list

print(words_list)

def get_valid_words(words_list):
    word = random.choice(words_list)
    # Keep selecting a new word if it contains a hyphen (-) or a space (' ')
    # as like "well-known" or "good day"
    while '-' in word or '' in word:
        word = random.choice(words_list)

    return word


def hangman():
    word = get_valid_words(words_list)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    