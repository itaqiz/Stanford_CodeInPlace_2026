import random

"""
🎲 Random Numbers Generator

Objective:
- Generate and print 10 random numbers
- Each number should be between 1 and 100

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

# Number of random values to generate
N_NUMBERS = 10

# Minimum possible random value
MIN_VALUE = 1

# Maximum possible random value
MAX_VALUE = 100


def main():
    # Generate and print random numbers
    for i in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))


# Entry point of the program
if __name__ == '__main__':
    main()