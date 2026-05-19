import random

"""
🎲 Dice Roll Simulator

Objective:
- Ask the user for the number of sides on a dice
- Generate a random number between 1 and the given number
- Display the result as the dice roll

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    # Take user input for number of sides on the dice
    selected = int(input("How many sides does your dice have? "))
    
    # Generate a random number between 1 and selected sides
    finding = random.randint(1, selected)
    
    # Display the dice roll result
    print("Your roll is " + str(finding))


# Entry point of the program
if __name__ == '__main__':
    main()