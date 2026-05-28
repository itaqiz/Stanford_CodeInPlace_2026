def main():
    """
    🌍 Quizzlet

    Objective:
    - Quiz the user on Spanish translations
    - Check answers
    - Keep score
    - Display final result

    👨‍💻 Coder Stamp:
    Written by: iTaqiZ - Pakistan 🇵🇰
    """

    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct_count = 0
    total = len(translations)

    # Loop through dictionary items
    for word in translations:
        answer = input(f"What is the Spanish translation for {word}? ")

        # Check correctness
        if answer == translations[word]:
            print("That is correct!")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {word} is {translations[word]}.")

        print()  # blank line for formatting

    # Final score
    print(f"You got {correct_count}/{total} words correct, come study again soon!")


if __name__ == '__main__':
    main()