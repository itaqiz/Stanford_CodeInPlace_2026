from graphics import Canvas

"""
⬜ Graphics Boxes Program

Objective:
- Create a canvas window
- Draw 5 equally sized boxes in a horizontal row

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

# Canvas dimensions
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200

# Number of boxes to draw
N_BOXES = 5

# Size of each box
BOX_SIZE = CANVAS_WIDTH / N_BOXES


def main():
    # Create drawing canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw boxes in a row
    for i in range(N_BOXES):
        # Calculate box coordinates
        left_x = i * BOX_SIZE
        top_y = 120
        right_x = left_x + BOX_SIZE
        bottom_y = top_y + BOX_SIZE
        
        # Draw rectangle (white fill, black border)
        rect = canvas.create_rectangle(
            left_x,
            top_y,
            right_x,
            bottom_y,
            "White",
            "Black"
        )
    

# Entry point of the program
if __name__ == '__main__':
    main()