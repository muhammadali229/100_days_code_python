from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print('Welcome to the secret auction program')
data = []
while True:
    name = input('What is your name? ')
    bid = int(input('What\'s your bid? $'))
    data.append({
        'name': name,
        'bid': bid
    })
    user_response = input("Are there any other biddrs? Type any key or 'no'. ").lower()
    if user_response ==  'no':
        break
    else:
        clear()

data.sort(key=lambda x: x['bid'], reverse=True)
print(f"The winner is {data[0]['name']} with a bid of ${data[0]['bid']}")