"""
🎯 Fill in the Blank Program

Example of a Fill in the Blank program.
The user enters three words (a color, an adjective, and a goal),
and the program generates a one-sentence story.

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    # Take user input for story elements
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")

    # Generate and display the story
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")


# Entry point of the program
if __name__ == "__main__":
    main()