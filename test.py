
import random


class KnapsackCipher:
    def __init__(self):
        # Generate private key (superincreasing sequence)
        self.private_key = self.generate_superincreasing_sequence(8)
        # Generate public key
        self.W, self.N = self.generate_multiplier_and_modulus()
        self.public_key = self.generate_public_key()

    def generate_superincreasing_sequence(self, length):
        """Generate a superincreasing sequence for private key"""
        sequence = [1]  # Start with 1
        for i in range(length - 1):
            # Each number should be greater than sum of all previous numbers
            next_num = sum(sequence) + random.randint(1, 10)
            sequence.append(next_num)
        return sequence

    def generate_multiplier_and_modulus(self):
        """Generate W (multiplier) and N (modulus)"""
        total_sum = sum(self.private_key)
        # N should be greater than sum of all numbers in private key
        N = total_sum + random.randint(10, 100)
        # W should be coprime with N and less than N
        W = random.randint(2, N-1)
        while self.gcd(W, N) != 1:
            W = random.randint(2, N-1)
        return W, N

    def generate_public_key(self):
        """Generate public key by multiplying private key with W mod N"""
        return [(x * self.W) % self.N for x in self.private_key]

    def gcd(self, a, b):
        """Calculate Greatest Common Divisor"""
        while b:
            a, b = b, a % b
        return a

    def mod_inverse(self, a, m):
        """Calculate modular multiplicative inverse"""
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        _, x, _ = extended_gcd(a, m)
        return (x % m + m) % m

    def encrypt(self, message):
        """Encrypt the message (string of 0s and 1s)"""
        if not all(bit in '01' for bit in message):
            raise ValueError("Message must be a binary string")
        
        # Pad message if necessary
        block_size = len(self.public_key)
        while len(message) % block_size != 0:
            message += '0'

        ciphertext = []
        # Process message in blocks
        for i in range(0, len(message), block_size):
            block = message[i:i + block_size]
            sum_value = 0
            for j, bit in enumerate(block):
                if bit == '1':
                    sum_value += self.public_key[j]
            ciphertext.append(sum_value)
        
        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt the ciphertext"""
        W_inverse = self.mod_inverse(self.W, self.N)
        plaintext = ""
        
        for c in ciphertext:
            # S = C * W^-1 mod N
            S = (c * W_inverse) % self.N
            # Solve knapsack problem using superincreasing sequence
            block = ""
            remaining_sum = S
            for w in reversed(self.private_key):
                if remaining_sum >= w:
                    block = '1' + block
                    remaining_sum -= w
                else:
                    block = '0' + block
            plaintext += block
        
        return plaintext.rstrip('0')  # Remove padding

# Example usage
def main():
    # Create Knapsack cipher instance
    knapsack = KnapsackCipher()
    
    print("Private Key:", knapsack.private_key)
    print("Public Key:", knapsack.public_key)
    print("W:", knapsack.W)
    print("N:", knapsack.N)
    
    # Example message (binary string)
    message = "10110011"
    print("\nOriginal Message:", message)
    
    # Encryption
    encrypted = knapsack.encrypt(message)
    print("Encrypted Message:", encrypted)
    
    # Decryption
    decrypted = knapsack.decrypt(encrypted)
    print("Decrypted Message:", decrypted)
    
    # Verify
    print("Decryption successful:", message == decrypted)

if __name__ == "__main__":
    main()
