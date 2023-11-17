import random
from milestone_3_hangman import word_list
from milestone_3_hangman import word

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = word
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word_guessed)
        self.num_lives = int(5)
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        self.guess = guess.lower()
        if guess in word:
            print(f'Good guess! {guess} is in the word')
        else:
            print(f'Sorry, {guess} is not in the word')
            self.num_lives - 1
            print(f'You have {self.num_lives} lives left')
        for letter in word:
            if letter == guess:
                self.word_guessed[letter] = letter
        self.num_letters - 1

    def ask_for_input(self):
        while True:
            guess = input("Please insert a letter ")
            print(guess)
            if len(guess) == 1 and guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
               self.check_guess(guess)
               self.list_of_guesses.append(guess)

first_guess = Hangman()
first_guess.ask_for_input()






