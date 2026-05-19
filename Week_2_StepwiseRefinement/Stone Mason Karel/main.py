from karel.stanfordkarel import *

"""
File: main.py
--------------------
🧱 Stone Mason Karel

Objective:
Karel repairs each column in the temple by placing beepers
from bottom to top of every column.

Approach:
- Move to each column
- Climb up while placing beepers
- Return to ground
- Move to next column

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    # Repeat process for 4 columns
    for i in range(4):
        build_each_column()   # Repair current column
        reset()               # Return to ground & move to next column
    

def build_each_column():
    # Turn to face upward (north)
    turn_left()
    
    # Place beeper at bottom of column
    put_beeper()
    
    # Move up the column and place beepers
    while front_is_clear():
        move()
        put_beeper()
    

def turn_around():
    # Turn 180 degrees
    turn_left()
    turn_left()
    

def reset():
    # Turn back to go down the column
    turn_around()
    
    # Move back to ground level
    while front_is_clear():
        move()
    
    # Face east to move to next column
    turn_left()
    
    # Move to next column if path exists
    if front_is_clear():
        for i in range(4):
            move()


if __name__ == '__main__':
    main()