alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ''
    alphabet_length = len(alphabet) - 1
    for c in text:
        remaining = alphabet_length - alphabet.index(c)
        if remaining > (shift - 1):
            cipher_text += alphabet[alphabet.index(c)+shift]
        else:
            cipher_text += alphabet[(shift - remaining - 1)]
    print(cipher_text)

def decrypt(text, shift):
    cipher_text = ''
    for c in text:
        cipher_text += alphabet[alphabet.index(c)-shift]
    print(cipher_text)

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
# ezqz
# hnanqnefynts