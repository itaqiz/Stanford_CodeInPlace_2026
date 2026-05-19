from graphics import Canvas
import math

"""
🌳 Clouds and Trees Scene

Objective:
- Draw decorative clouds on the canvas
- Create a reusable cloud drawing function
- Prepare the scene for adding trees and extra elements

👨‍💻 Coder Stamp:
Written by: iTaqiZ - Pakistan 🇵🇰
"""
    
# Canvas dimensions
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

# Cloud dimensions
CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

# Tree dimensions
TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

# Ground position for trees
TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 


def main():
    # Create drawing canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw first cloud
    draw_cloud(canvas, 140, 10, 'salmon')
    
    # TODO: draw two more clouds, and three trees


def draw_cloud(canvas, x, y, color):
    """
    Draws a cloud using three overlapping ovals.

    Parameters:
    - canvas : drawing canvas
    - x, y   : top-left position of cloud
    - color  : cloud color
    """
    
    # Calculate cloud positioning values
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH

    # Draw bottom-left puff
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Draw bottom-right puff
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Draw top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )


# TODO: Define a tree drawing function
# and add extra scenery elements if desired.


# Entry point of the program
if __name__ == '__main__':
    main()