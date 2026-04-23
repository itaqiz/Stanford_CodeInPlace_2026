from karel.stanfordkarel import *

"""
🧩 2026 Karel

Objective:
Karel should:
- Place 20 beepers at the starting position
- Move one step forward
- Place 26 beepers at the next position
- Move one step forward and end facing East

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    # Place first set of 20 beepers
    for _ in range(20):
        put_beeper()
    
    # Move to next position
    move()
    
    # Place second set of 26 beepers
    for _ in range(26):
        put_beeper()
    
    # Move to final position (facing East)
    move()


# 🚫 Do not edit below this line
if __name__ == '__main__':
    main()