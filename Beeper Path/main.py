from karel.stanfordkarel import *

"""
🎯 Objective:
Karel follows a straight line of beepers and moves forward
as long as it is standing on a beeper.

Assumption:
Karel starts on a beeper and the path is continuous.

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    # Continue moving forward while standing on a beeper
    while beepers_present():
        move()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()