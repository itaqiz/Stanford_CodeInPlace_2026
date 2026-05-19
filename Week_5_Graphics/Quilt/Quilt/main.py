# Quilt
from graphics import Canvas

"""
🧵 Quilt Pattern Program

Objective:
- Create a quilt-style canvas pattern
- Alternate between square patches and circle patches
- Arrange patches in two rows

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""

# Each patch is a square with this width and height
PATCH_SIZE = 100

# Canvas dimensions
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2


def main():
    # Create drawing canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw the first row of patches
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE * 2, 0)
    draw_circle_patch(canvas, PATCH_SIZE * 3, 0)

    # Draw the second row of patches
    draw_circle_patch(canvas, 0, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_circle_patch(canvas, PATCH_SIZE * 2, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE * 3, PATCH_SIZE)
    

def draw_circle_patch(canvas, start_x, start_y):
    """
    Draws a circular patch inside one quilt section.
    """

    # Calculate patch boundaries
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE

    # Draw salmon-colored circle
    canvas.create_oval(start_x, start_y, end_x, end_y, 'salmon') 
    
    pass


def draw_square_patch(canvas, start_x, start_y):
    """
    Draws a framed square patch.
    """

    # Calculate patch boundaries
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE

    # Margin for inner white square
    inset = 20

    # Draw outer purple square
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')

    # Draw inner white square
    canvas.create_rectangle(
        start_x + inset,
        start_y + inset,
        end_x - inset,
        end_y - inset,
        'white'
    )
    

# Entry point of the program
if __name__ == '__main__':
    main()