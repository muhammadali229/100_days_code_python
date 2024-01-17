from cipher_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    cipher_text = ''
    alphabet_length = len(alphabet) - 1
    end_text = ''
    for c in text:
        if c in alphabet:
            if direction == 'encode':
                remaining = alphabet_length - alphabet.index(c)
                if remaining > (shift - 1):
                    cipher_text += alphabet[alphabet.index(c)+shift]
                else:
                    cipher_text += alphabet[(shift - remaining - 1)]
            elif direction == 'decode':
                cipher_text += alphabet[alphabet.index(c)-shift]
        else:
            end_text += c
    else:
        cipher_text += end_text

    print(cipher_text)
# ezqz
# hnanqnefynts

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user = input("Type 'yes' if you want to go again. Otherwise type 'no' ")
    if user == 'no':
        print('Program Exit')
        break