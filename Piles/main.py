from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# Karel picks up ALL beepers from each pile,
# regardless of how many beepers are present.

"""
👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

def main():
    move()
    pick_all_beepers()

    move()
    move()
    pick_all_beepers()

    move()
    move()
    pick_all_beepers()

    move()


def pick_all_beepers():
    # Keep picking beepers until none remain
    while beepers_present():
        pick_beeper()


# don't edit these next two lines
if __name__ == '__main__':
    main()