"""
🐶 Dog Years Calculator

Objective:
Convert human years into dog years using a multiplier.

Formula:
1 human year = 7.18 dog years

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    # Take user input (convert to integer)
    dog_age = int(input("Enter an age in calendar years: "))
    
    # Calculate dog years
    result = dog_age * 7.18
    
    # Display the result
    print("That's " + str(result) + " in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()