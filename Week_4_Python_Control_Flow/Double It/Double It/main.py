"""
🔢 Double Until 100 Program

Objective:
- Take a number from the user
- Keep doubling the number while it is less than 100
- Print each updated value

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    # Take user input and convert it to integer
    curr_value = int(input("Enter a number: "))

    # Keep doubling the value until it reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2
        
        # Display the updated value
        print(curr_value)
    

# Entry point of the program
if __name__ == '__main__':
    main()