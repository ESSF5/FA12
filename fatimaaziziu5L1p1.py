Task: Draw a square using a loop instead of repeated commands.
import turtle
t = turtle.Turtle()
for _ in range(4):  # Loop 4 times
    t.forward(100)  # Move forward 100 pixels
    t.left(90)      # Turn left by 90 degrees
turtle.done()
u5L1p2.py
Task 1: Fix the triangle code to draw an equilateral triangle.
import turtle
t = turtle.Turtle()
for _ in range(3):  # Loop 3 times
    t.forward(100)  # Move forward 100 pixels
    t.left(120)     # Turn left by 120 degrees for a triangle
turtle.done()
Task 2: Modify the triangle code (introduce an error).
import turtle
t = turtle.Turtle()
for _ in range(60):  # Loop 60 times
    t.forward(100)   # Move forward 100 pixels
    t.left(123)      # Turn left by 123 degrees
turtle.done()
Task 3: Modify the square code (introduce an error).
import turtle
t = turtle.Turtle()
for _ in range(80):  # Loop 80 times
    t.forward(100)   # Move forward 100 pixels
    t.left(93)       # Turn left by 93 degrees
turtle.done()
u5L1p3.py
Task: Plot a red dot at (100, 100) with no lines on the canvas.
import turtle
t = turtle.Turtle()
t.penup()            # Lift the pen to stop drawing
t.goto(100, 100)     # Move to the coordinates (100, 100)
t.dot(20, "red")     # Plot a red dot with size 20
turtle.done()
