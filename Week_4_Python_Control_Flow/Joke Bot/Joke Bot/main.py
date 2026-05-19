"""
😂 Joke Bot

Objective:
- Ask the user what they want
- If the user types "Joke", print a programming joke
- Otherwise, print a default apology message

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

# Prompt shown to the user
PROMPT = "What do you want? "

# Joke message
JOKE = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"

# Default response if input is not "Joke"
SORRY = "Sorry I only tell jokes"


def main():
    # Take user input
    user_input = input(PROMPT)
    
    # Check if user asked for a joke
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)


# Entry point of the program
if __name__ == "__main__":
    main()