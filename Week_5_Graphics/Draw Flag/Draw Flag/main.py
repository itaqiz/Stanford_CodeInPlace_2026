from graphics import Canvas
import random

"""
🎨 Graphics Rectangle Program

Objective:
- Create a canvas window
- Draw a red rectangle covering the top half of the canvas

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

# Canvas dimensions
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300


def main():
    # Create drawing canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT) 
    
    # Rectangle coordinates
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT / 2
    
    # Draw red rectangle on top half of canvas
    rect = canvas.create_rectangle(
        left_x,
        top_y,
        right_x,
        bottom_y,
        "Red"
    )
    

# Entry point of the program
if __name__ == '__main__':
    main()