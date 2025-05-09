# Caesar cipher
# This code implements a simple Caesar cipher encryption and decryption.
# The Caesar cipher is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet.
# In this code, a dictionary is used to map each letter to another letter "key" positions ahead for encryption and "key" positions behind for decryption.
# The code handles both uppercase and lowercase letters, while leaving non-letter characters unchanged.
# The main function demonstrates the encryption and decryption process.

import string

# Get all ASCII letters: lowercase and uppercase
all_letters = string.ascii_letters

# Create an empty dictionary for encryption/decruption mapping
dict = {}

# Fixed key for Caesar Cipher (shift by 4 letters)
key = 4

def encryption(plain_txt):
    cipher_txt = []

    # Create the encryption mapping dictionary
    for j in range(len(all_letters)):
        # Map each letter to another letter "key" positions ahead
        dict[all_letters[j]]=all_letters[(j+key)%len(all_letters)]
    # Process each character in the input plain text
    for char in plain_txt:
        if char in all_letters:
            # Substitute letters using the dictionary
            temp = dict[char]
            cipher_txt.append(temp)
        else:
            # Keep non-letter character (like spaces, punctuation) unchanged
            cipher_txt.append(char)


    # Join list into a single string and return the encrypted text
    cipher_txt = "".join(cipher_txt)
    return cipher_txt


def decryption(encrypted_txt):
    decrypt_txt = []
     
    # Rebuild the dictinary for decryption (reverse mapping)
    for j in range(len(all_letters)):
        # Map each letter to the one "key" positions behind
        dict[all_letters[j]]= all_letters[(j-key)%(len(all_letters))]

    # Process each character in the input encrypted text
    for char in encrypted_txt:
        if char  in all_letters:
            # Substitute using the reverse dictionary
            temp = dict[char]
            decrypt_txt.append(temp)
        else:
            # Leave non-letter character unchanged
            temp = char
            decrypt_txt.append(temp)

    # join list into a single string and return the decrypted text
    decrypt_txt = "".join(decrypt_txt)
    return decrypt_txt


def main():
    encrypted_txt = encryption("I am studying substitution cipher")
    print(f"Cipher Text: {encrypted_txt}")

    decrypt_txt = decryption(encrypted_txt)
    print(f"Decrypted text: {decrypt_txt}")

if __name__ == "__main__":
    main()

