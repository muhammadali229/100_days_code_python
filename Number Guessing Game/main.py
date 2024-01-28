import random
from art import logo
print(logo)

print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100')

def set_difficulty():
    difficulty = input("Choose a difficulty Type 'easy' or 'hard': ").lower()
    dict_diff = {
        'easy': 10,
        'hard': 5
    }
    return dict_diff[difficulty]

def generate_random_no():
    return random.randint(1, 100)

def check_answer(user_guess, rand_num):
    is_over = False
    if user_guess < rand_num:
        print('Too low.')
    elif user_guess > rand_num:
        print('Too High.')
    else:
        print('You Won')
        is_over = True
    return is_over


def game():
    rand_num = generate_random_no()
    i = set_difficulty()
    while i > 0:
        print(f'You have {i} attempts remaining to guess the number.')
        user_guess = int(input('Make a guess: '))
        is_game_over = check_answer(user_guess, rand_num)
        if is_game_over:
            break
        if i == 1:
            print(f"You've ran out of guesses, you lose. The guess number is {rand_num}")
        else:
            print('Guess again.')
        i -= 1
game()