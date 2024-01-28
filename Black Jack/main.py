############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# import libraries and modules
import random
from art import logo
from replit import clear


# Create a deal_card() function that uses the List below to *return* a random card. 11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
#Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards_in):
    score = sum(cards_in)
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and 
    # return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(cards_in) == 2 and sum(cards_in) == 21:
        return 0
    # check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    elif score > 21 and 11 in cards_in:
        cards_in.remove(11)
        cards_in.append(1)
    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        print('Draw')
    elif computer_score == 0:
        print('User lost Computer has a black jack')
    elif user_score == 0 :
        print('User Wins User has a black jack')
    elif user_score > 21:
        print('User lost get over 21')
    elif computer_score > 21:
        print('Computer lost get over 21')
    elif user_score > computer_score:
        print('User score greater than computer score')
    elif computer_score > user_score:
        print('Computer score greater than user score')


def black_jack_game():
    # clear the screen
    clear()
    # print logo
    print(logo)


    #  Deal the user and computer 2 cards.
    user_cards = []
    computer_cards = []

    is_game_over = False

    user_cards.extend([deal_card() for _ in range(2)])
    computer_cards.extend([deal_card() for _ in range(2)])

    while not is_game_over:

        # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'User cards: {user_cards}, user score: {user_score}')
        print(f'Computer first card: {computer_cards[0]}')

        if  user_score == 0 or computer_score == 0 or user_score > 21:
            print('Game Ends')
            is_game_over = True
        else:
            # If the game has not ended, ask the user if they want to draw another card. If yes, 
            # then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            user_input = input("Type 'y' to draw another card or any key to end the game ").lower()
            if user_input == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'User Cards: {user_cards}, user score: {user_score}')
    print(f'Computer Cards: {computer_cards}, computer score: {computer_score}')
    compare(user_score, computer_score)

    #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    user_restart = input("Type 'y' to restart the game or any key to end the game ").lower()
    if user_restart == 'y':
        return black_jack_game()
    return

black_jack_game()