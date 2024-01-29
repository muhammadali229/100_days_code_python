from art import logo, vs
from replit import clear
from game_data import data
import random

clear()

def chose_random_data():
    return random.choice(data)
    # return data[random.randint(0, len(data) - 1)]

def compare_answers(user_input, follower_count_A, follower_count_B):
    if (user_input == 'a' and follower_count_A > follower_count_B) or (user_input == 'b' and follower_count_B > follower_count_A):
        return True
    return False
    
def game():
    score = 0
    is_game_over = False
    while not is_game_over:
        if score >= 1:
            print(f"You're right, current score: {score}")
        chose_random_data_A = chose_random_data()
        chose_random_data_B = chose_random_data()
        if chose_random_data_A == chose_random_data_B:
            chose_random_data_B = chose_random_data()
        print(f'Compare A: {chose_random_data_A["name"]}, a {chose_random_data_A["description"]}, from {chose_random_data_A["country"]}')
        print(vs)
        print(f'Against B: {chose_random_data_B["name"]}, a {chose_random_data_B["description"]}, from {chose_random_data_B["country"]}')
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_win = compare_answers(user_input, chose_random_data_A["follower_count"], chose_random_data_B["follower_count"])
        if is_win:
            score += 1
            clear()
        else:
            clear()
            print(f"Sorry, that's wrong. Final Score: {score}")
            is_game_over = True
game()