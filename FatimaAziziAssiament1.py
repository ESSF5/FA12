import math  # Import the math library for calculations

# 1. Calculate the area of a rectangle
print("Rectangle Area Calculation")
length = float(input("Enter the length of the rectangle: "))  # User inputs length
width = float(input("Enter the width of the rectangle: "))  # User inputs width
area_rectangle = length * width  # Formula for area of a rectangle
print(f"The area of the rectangle is: {area_rectangle:.2f}\n")  # Print result to 2 decimal places

# 2. Calculate the area of a circle
print("Circle Area Calculation")
radius_circle = float(input("Enter the radius of the circle: "))  # User inputs radius
area_circle = math.pi * math.pow(radius_circle, 2)  # Formula for area of a circle
print(f"The area of the circle is: {area_circle:.2f}\n")  # Print result to 2 decimal places

# 3. Calculate the surface area and volume of a cylinder
print("Cylinder Surface Area and Volume Calculation")
radius_cylinder = float(input("Enter the radius of the cylinder: "))  # User inputs radius
height_cylinder = float(input("Enter the height of the cylinder: "))  # User inputs height
volume_cylinder = math.pi * math.pow(radius_cylinder, 2) * height_cylinder  # Volume formula
surface_area_cylinder = 2 * math.pi * radius_cylinder * (radius_cylinder + height_cylinder)  # Surface area formula
print(f"The volume of the cylinder is: {volume_cylinder:.2f}")  # Print volume result
print(f"The surface area of the cylinder is: {surface_area_cylinder:.2f}\n")  # Print surface area result

# 4. Calculate the period of a pendulum
print("Pendulum Period Calculation")
length_pendulum = float(input("Enter the length of the pendulum (in meters): "))  # User inputs length
g = 9.8  # Gravity constant
period_pendulum = 2 * math.pi * math.sqrt(length_pendulum / g)  # Formula for pendulum period
print(f"The period of the pendulum is: {period_pendulum:.2f} seconds")  # Print result to 2 decimal places
Rectangle Area Calculation
Enter the length of the rectangle: 5
Enter the width of the rectangle: 3
The area of the rectangle is: 15.00

Circle Area Calculation
Enter the radius of the circle: 4
The area of the circle is: 50.27

Cylinder Surface Area and Volume Calculation
Enter the radius of the cylinder: 3
Enter the height of the cylinder: 7
The volume of the cylinder is: 197.92
The surface area of the cylinder is: 188.40

Pendulum Period Calculation
Enter the length of the pendulum (in meters): 10
The period of the pendulum is: 6.34 seconds
