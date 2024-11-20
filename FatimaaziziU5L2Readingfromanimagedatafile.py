import matplotlib.pyplot as plt

# Function to replace '~' with a space
def replace_tilde_with_space(symbol):
    return ' ' if symbol == '~' else symbol

# Open the file for reading
filename = "smiley_emoji_mod.xpm"
with open(filename, "r") as fh:
    # Read dimensions and number of colors
    first_line = fh.readline().strip()
    cols, rows, num_colors = map(int, first_line.split())
    print(f"Dimensions: {cols}x{rows}")
    print(f"Number of colors: {num_colors}")

    # Read color definitions
    color_map = {}
    for _ in range(num_colors):
        color_line = fh.readline().strip()
        sym, _, color = color_line.split()
        sym = replace_tilde_with_space(sym)  # Replace tilde with space if necessary
        color_map[sym] = color
    print("\nColor Map:")
    for sym, color in color_map.items():
        print(f"'{sym}': {color}")

    # Read image data
    image_data = []
    for _ in range(rows):
        line = fh.readline().strip()
        image_data.append([replace_tilde_with_space(ch) for ch in line])
    print("\nImage Data:")
    for row in image_data:
        print(''.join(row))

# Plot the image using matplotlib
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Convert color names to RGB using a predefined dictionary (for simplicity)
color_to_rgb = {
    'white': 'white',
    'black': 'black',
    # Add other colors as necessary
}

# Draw the image pixel by pixel
for y in range(rows):
    for x in range(cols):
        sym = image_data[y][x]
        color = color_to_rgb.get(color_map[sym], 'gray')  # Default to gray if color not found
        ax.add_patch(plt.Rectangle((x, rows - y - 1), 1, 1, color=color))

# Set axis limits and hide gridlines
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.axis('off')

# Show the plot
plt.show()
