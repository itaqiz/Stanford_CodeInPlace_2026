"""
🔢 Multiply Two Numbers Program
--------------------
This program asks the user for two integers
and prints their product.

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    # Display program purpose
    print("This program multiplies two numbers.")
    
    # Take user inputs and convert to integers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Calculate multiplication
    result = num1 * num2
    
    # Display the result
    print(result)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()