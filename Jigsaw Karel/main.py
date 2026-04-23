from karel.stanfordkarel import *

"""
🧩 Karel Puzzle Solver

Objective:
Karel picks up the last beeper (puzzle piece) and places it 
in the correct location.

Constraint:
Karel must end at the same starting position 
(bottom-left corner).

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""


def main():
    # Move to the beeper location
    move()
    move()
    
    # Pick the puzzle piece (beeper)
    pick_beeper()
    
    # Move towards the target location
    move()
    turn_left()
    move()
    move()
    
    # Place the beeper at correct spot
    put_beeper()
    
    # Turn around (180°)
    turn_left()
    turn_left()
    
    # Return path
    move()
    move()
    
    # Adjust direction (face south)
    turn_left()
    turn_left()
    turn_left()
    
    # Move back to starting column
    move()
    move()
    move()
    
    # Face original starting direction
    turn_left()
    turn_left()
    
    pass


# 🚫 Do not edit below this line
if __name__ == '__main__':
    main()