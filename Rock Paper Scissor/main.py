import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
computer_input = random.randint(0, 2)

if user_input >= 3 or user_input < 0:
    print('Invalid User input')
else:
    rps_lst = [rock, paper, scissors]
    user_choice = rps_lst[user_input]
    computer_choice = rps_lst[computer_input]
    print(user_choice)
    print('Computer Choice: ')
    print(computer_choice)
    if ((user_input == 0 and computer_input == 2) or 
    (user_input == 1 and computer_input == 0) or 
    (user_input == 2 and computer_input == 1)):
        print('You win') 
    elif ((user_input == 2 and computer_input == 0) or 
        (user_input == 0 and computer_input == 1) or 
        (user_input == 1 and computer_input == 2)):
        print('You lose') 
    else:
        print('Draw')