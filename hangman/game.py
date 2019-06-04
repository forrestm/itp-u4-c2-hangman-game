from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['chicken', 'horse', 'donkey', 'monkey', 'lion']


def _get_random_word(list_of_words):
    return random.choice(list_of_words)


def _mask_word(word):
    secret_word = ''
    for letter in word:
        secret_word += '*'
    return secret_word


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) == 0:
        raise InvalidWordException
    elif len(character) > 1:
        raise InvalidGuessedLetterException
    elif len(answer_word) != len(masked_word):
        raise InvalidWordException
    for order, letter in answer_word:
        if letter == character:
            new_masked_word = answer_word.replace(letter, )
            
        

def guess_letter(game, letter):
    


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game

