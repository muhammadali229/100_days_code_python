import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
# print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Enter any letter to guess the word? ").lower()
# print(guess)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for c in chosen_word:
    if guess == c:
        print('Right')
    else:
        print('Wrong')