import random

"""
🧮 Khansole Academy - Addition Quiz

Objective:
- Generate two random two-digit numbers
- Ask the user to solve the addition problem
- Check whether the answer is correct
- Display the correct answer if the user is wrong

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    print("Khansole Academy")

    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    total = num1 + num2

    print(f"What is {num1} + {num2}?")
    answer = int(input("Your answer: "))
    if answer == total:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {total}") 
    
if __name__ == '__main__':
    main()