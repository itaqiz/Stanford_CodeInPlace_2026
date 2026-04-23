from karel.stanfordkarel import *

"""
🌍 Karel World Filler

Objective:
Karel fills the entire world with beepers row by row.

Strategy:
- Fill one row completely with beepers
- Return to the start of the row
- Move up to the next row
- Repeat until the world is fully filled

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""


def main():
    """
    Repeats the process of:
    1. Filling a row
    2. Moving to the next row
    until no more rows are left.
    """
    while left_is_clear():
        fill_the_row()
        reset_to_next_row()
    
    # Fill the last row (edge case)
    fill_the_row()


def fill_the_row():
    # Place beeper at current position
    put_beeper()
    
    # Move across the row placing beepers
    while front_is_clear():
        move()
        put_beeper()


def reset_to_next_row():
    # Go back to the start of the row
    turn_around()
    
    while front_is_clear():
        move()
    
    # Move up to next row
    turn_right()
    move()
    turn_right()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()