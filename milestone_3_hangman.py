import random

word_list = ["pineapple", "coconut", "banana", "orange", "mango"]
word = random.choice(word_list)
print(word)

guess = input("Please insert a letter ")
print(guess)

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    while True:
        guess = input("Please insert a letter ")
        print(guess)
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character")
    check_guess(guess)

ask_for_input()