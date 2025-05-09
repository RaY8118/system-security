# This program encrypts and decrypts messages using a substitution cipher.
# The user can input a custom key or generate a random one.
# The program checks if the key is valid (contains all letters of the alphabet).
# It then translates the message based on the key and the chosen mode (encrypt or decrypt).

import random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getRandomKey():
    randomList = list(LETTERS)
    random.shuffle(randomList)
    return "".join(randomList)


def checkKey(key):
    keyString = "".join(sorted(list(key)))
    return keyString == LETTERS


def translateMessage(message, key, mode):
    # Create a translation table
    translated = ""
    charsA = LETTERS
    charsB = key

    if mode == "D":
        charsA, charsB = charsB, charsA
    # Translate the message
    for symbol in message:
        # If the symbol is in charsA, find the index and translate it
        if symbol.upper() in charsA:
            # Get the index of the symbol in charsA
            index = charsA.find(symbol.upper())
            # Translate the symbol using charsB
            if symbol.isupper():
                # If the symbol is uppercase, use the uppercase letter from charsB
                translated += charsB[index]
            else:
                # If the symbol is lowercase, use the lowercase letter from charsB
                translated += charsB[index].lower()
        else:
            translated += symbol
    return translated


def main():
    # Get the message to encrypt or decrypt
    message = "" 
    message = input("Enter your message: ")
    mode = input("E for Encrypt, D for Decrypt: ")
    key = ""

    # Check if the mode is valid
    while checkKey(key) is False:
        # Get the key from the user or generate a random one
        key = input("Enter 26 ALPHA key (leave blank for random key): ")
        if key == "":
            key = getRandomKey()
            break

    print(f"Using key: {key}")
    translated = translateMessage(message, key, mode)
    print(f"Result: {translated}")


if __name__ == "__main__":
    main()
