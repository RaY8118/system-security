# Function to find the modular inverse of a number 'a' modulo 'm'
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


# Key Generation (Superincreasing Sequence, Modulus, Multiplier)
def generate_public_key():
    # Superincreasing sequence
    S = [1, 2, 4, 10, 20, 40]
    m = 110  # Modulus (must be greater than the sum of elements in S)
    n = 31  # Multiplier (must be coprime with m)

    # Calculate the public key (modular multiplication of superincreasing sequence by n)
    public_key = [(n * s) % m for s in S]

    return S, public_key, m, n


# Encryption: Converts a binary message to a number and encrypts it
def encrypt(message, public_key):
    ciphertext = []
    # Split the message into chunks of 6 bits (as there are 6 elements in the public key)
    for i in range(0, len(message), 6):
        chunk = message[i : i + 6]
        cipher_value = sum(int(chunk[j]) * public_key[j] for j in range(len(chunk)))
        ciphertext.append(cipher_value)
    return ciphertext


# Decryption: Decrypts the ciphertext using the private key (superincreasing sequence and inverse of n)
def decrypt(ciphertext, S, m, n):
    # Calculate the inverse of the multiplier n modulo m
    n_inv = mod_inverse(n, m)

    # Decrypt the ciphertext by multiplying each element with n_inv modulo m
    decrypted_message = []
    for value in ciphertext:
        # Multiply by the modular inverse of n and take modulo m
        reduced_value = (value * n_inv) % m

        # Find the corresponding sum from the private key
        bit_string = [0] * len(S)
        for i in range(
            len(S) - 1, -1, -1
        ):  # Start from the largest value in the private key
            if reduced_value >= S[i]:
                bit_string[i] = 1
                reduced_value -= S[i]

        # Join the bits and add to the decrypted message
        decrypted_message.append("".join(map(str, bit_string)))

    # Join all the decrypted chunks into one string
    return "".join(decrypted_message)


# Test the Knapsack Encryption and Decryption
def main():
    # Generate keys
    S, public_key, m, n = generate_public_key()
    print("Private key (Superincreasing sequence):", S)
    print("Public key:", public_key)

    # Message to encrypt (binary string)
    message = "100100111100101110"  # Example binary message
    print("\nOriginal message:", message)

    # Encrypt the message
    ciphertext = encrypt(message, public_key)
    print("Ciphertext:", ciphertext)

    # Decrypt the message
    decrypted_message = decrypt(ciphertext, S, m, n)
    print("\nDecrypted message:", decrypted_message)


# Run the Knapsack encryption and decryption example
if __name__ == "__main__":
    main()
