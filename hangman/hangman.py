import random
import string

def load_word():
    f = open('hangman_words.txt', 'r')
    wordsList = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    guessed = False
    for letter in secret_word:
        if letter in letters_guessed:
            guessed = True
        else:
            guessed = False
            break
    return guessed

def gen_alphabet():
    Alphabet = list(string.ascii_lowercase)
    return Alphabet

def get_guessed_word(secret_word, letters_guessed):
    ''' returns string of letters and underscores '''
    guessed_with_blanks = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_with_blanks += letter
        else:
            guessed_with_blanks += "_"
    return guessed_with_blanks


def get_availaible_letters(letters_guessed, alphabet): #switch this to get rid of global
    not_yet_guessed = []

    for letter in alphabet:
        if letter not in letters_guessed:
            not_yet_guessed.append(letter)
    return not_yet_guessed

def take_guess():
    guess = input("guess a letter: ").lower()
    return guess

def add_to_guessed(guess):
    pass

'''
def hangman(secret_word, alphabet):
    playing = True
    while playing:
        print(get_guessed_word(secret_word, letters_guessed))

'''
print(load_word())






'''
def length_of_word(word):
    length = len(word) + 1
    return length
'''

'''
def letter_s(word):
    spaces = []
    for letter in word:
        spaces.append(letter)
    return spaces
'''

'''
for letter in "laurel":
    print(letter)
'''
