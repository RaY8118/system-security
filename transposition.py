# This program encrypts and decrypts messages using a transposition cipher.
# The user can input a key and a message, and the program will encrypt and decrypt the message using the transposition cipher algorithm.

import math


def encryptMessage(key, message):
    ciphertext = [''] * key
    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key

    return ''.join(ciphertext)

def decryptMessage(key,message):
    numOfColumns = int(math.ceil(len(message) / key))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


def main():
    message = "Transposition Cipher"
    key = 10
    ciphertext = encryptMessage(key, message)
    print(f"Cipher text is {ciphertext}")
    plaintext = decryptMessage(key,ciphertext)
    print(f"Plain text is {plaintext}")



if __name__ == "__main__":
    main()
