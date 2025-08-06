import math
import hashlib
import random

# Parameters used in this case
MIN_ENTROPY = 30

# Simulated leaked passwords
LeakedPwd = ["password123", "123", "123456", "qwerty", "letmein", "admin"]

# Simple Bloom filter setup
class BloomFilter:
    def __init__(self, size=500):
        self.size = size
        self.bit_array = [0] * size
        self.hash_count = 3

    def _hashes(self, word):
        hashes = []
        for seed in range(self.hash_count):
            result = int(hashlib.md5((word + str(seed)).encode()).hexdigest(), 16)
            hashes.append(result % self.size)
        return hashes

    def add(self, word):
        for hash_val in self._hashes(word):
            self.bit_array[hash_val] = 1

    def check(self, word):
        return all(self.bit_array[hash_val] == 1 for hash_val in self._hashes(word))

# Entropy Calculation
def calculate_entropy(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in "!@#$%^&*()-_+=" for c in password):
        charset_size += 15  # approximate common symbols

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)
    return entropy

# Main
if __name__ == "__main__":
    bloom = BloomFilter()
    for pwd in LeakedPwd:
        bloom.add(pwd)

    password = input("Enter a new password: ")

    # Entropy check
    entropy = calculate_entropy(password)
    print(f"\nPassword Entropy: {entropy:.2f} bits")

    if entropy < MIN_ENTROPY:
        print("Password entropy too low. Choose a longer or more complex password.")
        print("Use more characters, and mix uppercase, lowercase, digits, and symbols.")
    else:
        print("Password entropy is sufficient.")

    # Leaked password check
    if bloom.check(password):
        print("\nWarning: This password may have been leaked before!")
    else:
        print("\nThis password does not appear in the leaked list.")

