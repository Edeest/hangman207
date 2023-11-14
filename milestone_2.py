import random

word_list = ["pineapple", "coconut", "banana", "orange", "mango"]
print(word_list)
word = random.choice(word_list)
print(word)

guess = print(input("Please insert a letter "))
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")

