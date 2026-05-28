"""
📊 Compute Average Program

Objective:
- Load numbers from a file
- Compute their average
- Print the average result

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    # Load numbers from file into a list
    number_list = load_numbers_from_file("numbers.txt")

    # Calculate total sum of all numbers
    total = 0
    for number in number_list:
        total += number

    # Calculate average
    average = total / len(number_list)

    # Display the result
    print(f"Average: {average}")


def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """

    numbers = []

    # Open file in read mode
    with open(filepath, 'r') as file_reader:

        # Read file line by line
        for line in file_reader.readlines():
            cleaned_line = line.strip()

            # Ignore empty lines
            if cleaned_line != '':
                numbers.append(float(cleaned_line))

    return numbers


# Entry point of the program
if __name__ == '__main__':
    main()