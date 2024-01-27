from art import logo
print(logo)


def add(no1, no2):
    """
        This is an add function take 2 float no and returns a float no 
    """
    res = no1 + no2
    print(f"{no1} + {no2} = {no1 + no2}")
    return res

def sub(no1, no2):
    """
        This is an subtract function take 2 float no and returns a float no 
    """
    res = no1 - no2
    print(f"{no1} - {no2} = {no1 - no2}")
    return res

def mult(no1, no2):
    """
        This is an multiply function take 2 float no and returns a float no 
    """
    res = no1 * no2
    print(f"{no1} * {no2} = {no1 * no2}")
    return res

def div(no1, no2):
    """
        This is an divide function take 2 float no and returns a float no 
    """
    res = no1 / no2
    print(f"{no1} / {no2} = {no1 / no2}")
    return res

operations_dict = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
}

is_continue = False
while True:
    if not is_continue:
        no1 = float(input("What's the first no? "))
    else:
        no1 = result
    # operation = input("+\n-\n*\n/\nPick an operation: ")
    for i in operations_dict.keys():
        print(f"{i}")
    operation = input('Pick an operation: ')
    no2 = float(input("What's the next no? "))
    result = operations_dict[operation](no1, no2)
    # if operation == '+':
    #     result = add(no1, no2)
    # elif operation == '-':
    #     result = sub(no1, no2)
    # elif operation == '*':
    #     result = mult(no1, no2)
    # elif operation == '/':
    #     result = div(no1, no2)
    user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' or any key to start a new calculation, or type 'q' to exit. ").lower()
    if user_input == 'q':
        print('Exiting...')
        break
    elif user_input == 'y':
        is_continue = True
    else:
        is_continue = False