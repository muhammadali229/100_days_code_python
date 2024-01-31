from data import MENU, resources
from replit import clear

def is_coffee_resourcess(ingredients):
    for key, value in ingredients.items():
            if value > resources[key]:
                print(f"Sorry there is not enough {key.title()}.")
                return False
    return True

def show_resources():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")

def asking_money():
    print("Please insert coins")
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    user_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return user_money

def resources_utilize(ingredients, cost):
    global resources
    for key, value in ingredients.items():
        resources[key] -= value
    resources["money"] += round(cost, 2)

def processing_transaction(user_input, cost, ingredients):
    user_money = asking_money()
    if user_money >= cost:
        resources_utilize(ingredients, cost)
        if user_money > cost:
            print(f"Here is ${round(user_money - cost, 2)} dollars in change")
        print(f"Here is your {user_input.title()}. Enjoy!.")
    else:
        print("Sorry that's not enough money. Money refunded.")

def coffee_machine():
    clear()
    resources['money'] = 0
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "off":
            print("Turn off the machine")
            break
        elif user_input == "report":
            show_resources()
        elif user_input in MENU:
            ingredients = MENU[user_input]["ingredients"]
            cost = MENU[user_input]["cost"]
            is_coffee = is_coffee_resourcess(ingredients)
            if is_coffee:
                processing_transaction(user_input, cost, ingredients)
        else:
            print('Kindly insert correct command')    
coffee_machine()