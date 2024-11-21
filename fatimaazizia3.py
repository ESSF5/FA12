import turtle

# Function to plot a single point
def plotIt(t, x, y, d, color):
    """
    Plots a point at the given (x, y) coordinates with the specified diameter and color.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(d, color)
    t.penup()

# Function to read the XPM file
def readFile(filename):
    """
    Reads the .xpm file and extracts the following:
    - Dimensions (cols, rows)
    - Color mappings
    - Image data
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Read dimensions and number of colors
    cols, rows, num_colors = map(int, lines[0].strip().split())
    colors = {}
    image_data = []

    # Read color definitions
    for i in range(1, num_colors + 1):
        sym, _, color_string = lines[i].strip().split()
        colors[sym] = color_string

    # Read image data
    for i in range(num_colors + 1, num_colors + 1 + rows):
        image_data.append(lines[i].strip())

    return cols, rows, colors, image_data

# Function to draw the image
def drawImage(t, cols, rows, colors, image_data, scale=10, rotate=False):
    """
    Draws the image by plotting points based on the color and coordinates.
    - scale: Multiplier for spacing between points
    - rotate: If True, flips the image upside down
    """
    # Center the image
    x_offset = -(cols // 2) * scale
    y_offset = (rows // 2) * scale

    for row in range(rows):
        for col in range(cols):
            char = image_data[row][col]
            if char in colors:
                # Calculate coordinates
                x = x_offset + col * scale
                y = y_offset - row * scale

                # Apply rotation if requested
                if rotate:
                    x, y = -x, -y

                # Plot the point
                plotIt(t, x, y, scale, colors[char])

# Masin Function 
def main():
    # Setup Turtle 
    turtle.bgcolor("gray40")  # Dark gray background
    turtle.tracer(0, 0)       # Disable screen updates for speed
    t = turtle.Turtle()
    t.hideturtle()

    # Ask the user for input
    print("Choose the image to display:")
    print("1. Smiley Emoji")
    print("2. Rocky & Bullwinkle")
    choice = int(input("Enter 1 or 2: "))
    rotate = input("Would you like to rotate the image? (yes/no): ").strip().lower() == "yes"

    # Select file based on user choice
    if choice == 1:
        filename = "smiley_emoji_mod.xpm"
    elif choice == 2:
        filename = "rocky_bullwinkle_mod.xpm"
    else:
        print("Invalid choice. Exiting.")
        return

    # Read file and draw the image
    cols, rows, colors, image_data = readFile(filename)
    drawImage(t, cols, rows, colors, image_data, scale=10, rotate=rotate)

    # Update the canvas and wait for the user to close
    turtle.update()
    turtle.done()

# Run the program
if __name__ == "__main__":
    main()
  
